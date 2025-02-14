from bs4 import BeautifulSoup
import re

# Load HTML file
html_path = "austen.html"
with open(html_path, 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the required fields
data = {}

# Extracting author forms
author_meta_tag = soup.find('meta', {'name': 'dc.creator'})
if author_meta_tag:
    author_meta = author_meta_tag['content']
    # Split name and lifespan
    match = re.match(r"(.*), (\d{4}-\d{4})", author_meta)
    if match:
        author_meta_name = match.group(1).strip()
        author_meta_lifespan = match.group(2).strip()
    else:
        author_meta_name = author_meta
        author_meta_lifespan = None
else:
    author_meta_name = None
    author_meta_lifespan = None

author_div_tag = soup.select_one('#pg-header-authlist p strong')
author_div = author_div_tag.find_next_sibling(text=True).strip() if author_div_tag else None

data['author'] = {
    'meta_form': author_meta_name,
    'lifespan': author_meta_lifespan,
    'display_form': author_div
}

# Extracting publisher (from colophon image or text if available)
publisher_tag = soup.find('img', {'alt': '[Colophon: GEORGE ALLEN PUBLISHER  156 CHARING CROSS ROAD LONDON]'})
data['publisher'] = publisher_tag['alt'].split(':')[-1].strip() if publisher_tag else None

# Extracting release date
release_date_tag = soup.find('meta', {'name': 'dcterms.created'})
data['release_date'] = release_date_tag['content'] if release_date_tag else None

# Extracting credits
credits_tag = soup.find('p', string=lambda text: text and 'Credits' in text)
data['credits'] = credits_tag.text.strip().replace('Credits: ', '') if credits_tag else None

# Extracting table of contents with chapter names and hrefs
toc_tag = soup.find('p', class_='toc')
toc_items = toc_tag.find_all('a') if toc_tag else []
data['table_of_contents'] = [
    {'chapter_name': item.text.strip(), 'href': item['href']}
    for item in toc_items
]

from bs4 import BeautifulSoup

def format_chapter_start(html_content):
    """
    Formats only the chapter or section heading in LaTeX, leaving other HTML content intact.

    Args:
        html_content (str): Raw HTML content for a chapter or section.

    Returns:
        str: LaTeX-formatted chapter or section heading with other content unchanged.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize LaTeX output
    latex_output = ""

    # Look for the first <h1>, <h2>, or <h3> tag
    for heading in soup.find_all(['h1', 'h2', 'h3'], limit=1):  # Only handle the first heading
        heading_text = heading.get_text(strip=True)  # Extract the heading text
        if heading.name == 'h1':  # Format for LaTeX chapter
            latex_output += f"\\chapter*{{{heading_text}}}\n"
        elif heading.name == 'h2':  # Format for LaTeX section
            latex_output += f"\\section*{{{heading_text}}}\n"
        elif heading.name == 'h3':  # Format for LaTeX subsection
            latex_output += f"\\subsection*{{{heading_text}}}\n"

        # Remove the processed heading from the soup
        heading.decompose()

    # Combine LaTeX-formatted heading with the remaining untouched HTML content
    latex_output += str(soup)

    return latex_output


def load_element_and_content(html_path, start_id):
    """
    Loads the content of an HTML element and its related content based on a starting ID,
    then formats it for LaTeX.

    Args:
        html_path (str): Path to the HTML file.
        start_id (str): ID of the element to start capturing content.

    Returns:
        str: LaTeX-formatted content for the chapter or section.
    """
    with open(html_path, 'r', encoding='utf-8') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Locate the starting element by ID
    start_element = soup.find(id=start_id)
    if not start_element:
        return None

    # Find the closest logical parent (like a section or div) to include all related content
    parent = start_element.find_parent()
    if not parent:
        return None

    # Capture all subsequent sibling elements after the parent
    content = []
    for sibling in parent.find_next_siblings():
        # Stop if reaching another distinct section or unrelated element
        if sibling.name in ['h2', 'hr', 'div'] and sibling.get('id') != start_id:
            break
        content.append(str(sibling))

    # Combine the parent's content with the subsequent relevant siblings
    raw_content = parent.decode_contents() + ''.join(content)

    # Format the extracted content for LaTeX
    return raw_content


def remove_page_numbers(html_content):
    """
    Removes all page number elements from the given HTML content.

    Args:
        html_content (str): Raw HTML content.

    Returns:
        str: The modified HTML content with all page numbers removed.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find and remove all elements with the class "pagenum"
    for page_number in soup.find_all(class_='pagenum'):
        page_number.decompose()  # Remove the tag from the HTML

    # Return the modified HTML as a string
    return soup.prettify()

from bs4 import BeautifulSoup

def convert_italic_to_latex(html_content):
    """
    Converts <i> tags in the HTML content to LaTeX italicized format.

    Args:
        html_content (str): Raw HTML content.

    Returns:
        str: Modified content with <i> tags replaced by LaTeX \textit{}.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <i> tags and replace them with LaTeX formatting
    for italic in soup.find_all('i'):
        italic.replace_with(r'\textit{' + italic.text.strip() + '}')

    # Return the modified HTML content as a string
    return str(soup)

from bs4 import BeautifulSoup

def format_paragraphs_for_latex(html_content):
    """
    Converts all <p> tags in the normalized HTML content to LaTeX paragraph format.

    Args:
        html_content (str): Raw or normalized HTML content.

    Returns:
        str: LaTeX-formatted paragraphs.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Initialize a list to store LaTeX-formatted paragraphs
    latex_output = []

    # Convert each <p> tag into a LaTeX paragraph
    for paragraph in soup.find_all('p'):
        paragraph_text = paragraph.get_text(strip=True)  # Get and clean the paragraph text
        latex_output.append(paragraph_text)  # Add the paragraph text to the output list

    # Join paragraphs with a blank line between them (standard LaTeX paragraph separation)
    return "\n\n".join(latex_output)


def convert_image_to_latex(html_content):
    """
    Converts <img> tags in the HTML content to LaTeX image format.

    Args:
        html_content (str): Raw HTML content.

    Returns:
        str: Modified content with <img> tags replaced by LaTeX \includegraphics{}.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <img> tags and replace them with LaTeX formatting
    for img in soup.find_all('img'):
        # Extract the necessary attributes
        img_src = img.get('src', '')
        img_alt = img.get('alt', '').strip()
        img_width = img.get('width', '')

        # Create the LaTeX image string
        if img_width:
            latex_img = f"\\includegraphics[width={img_width}px]{{{img_src}}}"
        else:
            latex_img = f"\\includegraphics{{{img_src}}}"

        # Replace the <img> tag with the LaTeX string
        if img_alt:  # Add a caption if there's an alt attribute
            latex_img = f"\\begin{{figure}}[h]\n\\centering\n{latex_img}\n\\caption{{{img_alt}}}\n\\end{{figure}}"

        img.replace_with(latex_img)

    # Return the modified HTML content as a string
    return str(soup)
from bs4 import BeautifulSoup

def normalize_paragraphs(html_content):
    """
    Normalizes HTML content by combining lines and inline elements within <p> tags into single strings.

    Args:
        html_content (str): Raw HTML content.

    Returns:
        str: HTML content with normalized paragraphs.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Process each <p> tag
    for paragraph in soup.find_all('p'):
        # Combine all strings within the paragraph into a single line, preserving inline formatting
        normalized_text = " ".join(paragraph.stripped_strings)  # Join with a space to avoid line breaks
        paragraph.clear()  # Clear the existing content of the paragraph
        paragraph.append(normalized_text)  # Replace with normalized single-line text

    return str(soup)

from bs4 import BeautifulSoup

def format_drop_letter_with_image(html_content):
    """
    Formats the first letter of a chapter or section using an image for the drop letter
    based on the 'letra' class.

    Args:
        html_content (str): Raw HTML content for a chapter or section.

    Returns:
        str: LaTeX-formatted content with the drop letter image integrated.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Locate the first paragraph and the drop letter image
    first_paragraph = soup.find('p')
    letra_span = soup.find('span', class_='letra')
    letra_image = letra_span.find('img') if letra_span else None

    # Initialize LaTeX output
    latex_output = ""

    if letra_image:
        # Extract the image source and size information
        img_src = letra_image.get('src', '')
        img_width = letra_image.get('width', '50')  # Default width if not specified

        # Embed the drop letter image in LaTeX
        drop_letter_latex = f"\\includegraphics[width={img_width}px]{{{img_src}}}"

        # Remove the 'letra' span to avoid duplication
        letra_span.decompose()

        # Add the drop letter image to the output
        latex_output += f"\\noindent {drop_letter_latex} "

    if first_paragraph:
        # Add the remaining text of the first paragraph
        paragraph_text = " ".join(first_paragraph.stripped_strings)  # Normalize spaces
        latex_output += paragraph_text

        # Remove the processed first paragraph to avoid duplication in further content
        first_paragraph.decompose()

    # Include any remaining content after the first paragraph
    latex_output += "\n\n" + soup.get_text(strip=False)

    return latex_output



# Test the function
start_id = "CHAPTER_V"

content = load_element_and_content(html_path, start_id)
content = format_drop_letter_with_image(content)
content = format_chapter_start(content)
# content = format_chapter_start(content)
content = remove_page_numbers(content)
content = convert_italic_to_latex(content)
content = convert_image_to_latex(content)
content = normalize_paragraphs(content)
content = format_paragraphs_for_latex(content)

print(content)

# Sample HTML content
html_content = """
<p class="nind">
<span class="letra">
<img alt="W" id="img_images_i_051_b.png" src="images/i_051_b.png" width="100"/>
</span>
ITHIN a short walk from the cottage.
</p>
<p>The morning was fine, and the children were delighted with the idea of being happy all day together.</p>
"""

# Format with the drop letter image
latex_content = format_drop_letter_with_image(html_content)
print(latex_content)