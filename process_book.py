import sys
import re
import os
import html
from bs4 import BeautifulSoup

def read_html_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def read_template():
    with open('template.tex', 'r', encoding='utf-8') as f:
        return f.read()

def extract_title_and_author(soup):
    """Extract title and author from HTML metadata or title tag."""
    # Try to extract from metadata
    title_meta = soup.find('meta', {'name': 'dc.title'})
    author_meta = soup.find('meta', {'name': 'dc.creator'})

    if title_meta and author_meta:
        title_text = title_meta.get('content', 'Untitled')
        author_text = author_meta.get('content', 'Unknown Author')
    else:
        # Fallback to title tag
        title_text = soup.title.string if soup.title else 'Untitled'
        author_text = 'Unknown Author'  # Default if not found

    return title_text.strip(), author_text.strip()

def sanitize_filename(name):
    # Remove any invalid characters for file paths
    return re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')

def html_to_latex(html_content, images_path):
    """Convert HTML content to LaTeX."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # **Remove all CSS styles and scripts**
    for style in soup.find_all('style'):
        style.decompose()
    for script in soup.find_all('script'):
        script.decompose()

    # Remove Project Gutenberg headers and footers
    for elem in soup.find_all(['div', 'section'], class_=['pgheader', 'pg-footer', 'pg-boilerplate']):
        elem.decompose()

    # Remove any comments
    for comment in soup.find_all(string=lambda text: isinstance(text, type(soup.Comment))):
        comment.extract()

    # Remove page numbers and anchors with IDs starting with 'page_'
    for pagenum in soup.find_all(class_='pagenum'):
        pagenum.decompose()
    for anchor in soup.find_all('a', id=re.compile('^page_')):
        anchor.decompose()

    # **Decode HTML entities**
    text = soup.prettify()
    text = html.unescape(text)

    # **Convert HTML content to LaTeX commands**
    # Re-parse the cleaned text
    soup = BeautifulSoup(text, 'html.parser')

    # Replace images
    for img in soup.find_all('img'):
        img_path = img.get('src')
        if img_path:
            # Assuming images are in the 'images/' folder
            image_filename = os.path.basename(img_path)
            # Replace image with LaTeX figure
            latex_img = f'\\begin{{figure}}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{{images/{image_filename}}}\n\\end{{figure}}'
            img.replace_with(latex_img)

    # Replace headings properly
    for header_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        for header in soup.find_all(header_tag):
            level = int(header_tag[1])
            header_text = escape_special_characters(header.get_text().strip())
            if header_text:  # Only replace non-empty headers
                if level == 1:
                    latex_header = f'\\chapter{{{header_text}}}\n'
                elif level == 2:
                    latex_header = f'\\section{{{header_text}}}\n'
                elif level == 3:
                    latex_header = f'\\subsection{{{header_text}}}\n'
                elif level == 4:
                    latex_header = f'\\subsubsection{{{header_text}}}\n'
                else:
                    latex_header = f'\\paragraph{{{header_text}}}\n'
                header.replace_with(latex_header)

    # Replace paragraphs
    for p in soup.find_all('p'):
        p_text = ''.join([str(item) for item in p.contents])
        p_text = convert_inline_formatting(p_text)
        p_text = escape_special_characters(p_text)
        p.replace_with(f'{p_text}\n\n')

    # Handle italics and bold that are not within paragraphs
    for italic in soup.find_all(['i', 'em']):
        italic_text = escape_special_characters(italic.get_text().strip())
        italic.replace_with(f'\\textit{{{italic_text}}}')

    for bold in soup.find_all(['b', 'strong']):
        bold_text = escape_special_characters(bold.get_text().strip())
        bold.replace_with(f'\\textbf{{{bold_text}}}')

    # Handle <br> tags by replacing them with line breaks
    for br in soup.find_all('br'):
        br.replace_with('\n')

    # Convert the soup object back to a string
    content = str(soup)

    # Remove any remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # **Final cleanup of content**
    # Remove multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()

def convert_inline_formatting(text):
    """Convert inline HTML formatting to LaTeX."""
    # Replace italics and bold within text
    text = re.sub(r'<i>(.*?)</i>', r'\\textit{\1}', text, flags=re.DOTALL)
    text = re.sub(r'<em>(.*?)</em>', r'\\textit{\1}', text, flags=re.DOTALL)
    text = re.sub(r'<b>(.*?)</b>', r'\\textbf{\1}', text, flags=re.DOTALL)
    text = re.sub(r'<strong>(.*?)</strong>', r'\\textbf{\1}', text, flags=re.DOTALL)
    return text

def escape_special_characters(text):
    special_chars = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    # Use regex to replace each special character
    for char, escape in special_chars.items():
        text = re.sub(re.escape(char), escape, text)
    return text

def write_output(content, title, author):
    template = read_template()
    output = template.replace('% START_OF_CONTENT', content)
    output = output.replace('<BOOK TITLE>', escape_special_characters(title))
    output = output.replace('<AUTHOR NAME>', escape_special_characters(author))
    
    # Create folder structure based on author and title
    safe_author = sanitize_filename(author)
    safe_title = sanitize_filename(title)
    output_dir = f"projects/{safe_author}_{safe_title}"
    
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "book.tex")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
        print("Generated LaTeX file content:")
        print(output)

def main(input_filename):
    html_content = read_html_file(input_filename)
    soup = BeautifulSoup(html_content, 'html.parser')
    title, author = extract_title_and_author(soup)
    images_path = 'images/'  # Assuming images are in 'images/' folder
    processed_content = html_to_latex(html_content, images_path)
    write_output(processed_content, title, author)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python process_book.py input.html")
        sys.exit(1)
    input_filename = sys.argv[1]
    main(input_filename)
