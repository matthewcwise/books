from ebooklib import epub

def inspect_spine(epub_file):
    try:
        book = epub.read_epub(epub_file)
    except Exception as e:
        print(f"Error reading EPUB file: {e}")
        return

    print("\nSpine items:")
    for item_ref in book.spine:
        print(item_ref)

def inspect_epub(epub_file):
    try:
        book = epub.read_epub(epub_file)
    except Exception as e:
        print(f"Error reading EPUB file: {e}")
        return

    print("\nAll items in the EPUB:")
    for item in book.items:
        print(f"ID: {item.id}, Type: {item.get_type()}, File: {item.file_name}")


from ebooklib import epub
from bs4 import BeautifulSoup

def epub_to_latex(epub_file, output_file):
    try:
        book = epub.read_epub(epub_file)
    except Exception as e:
        print(f"Error reading EPUB file: {e}")
        return

    latex_content = [
        r"\documentclass{book}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage{hyperref}",
        r"\begin{document}",
        r"\tableofcontents",
    ]

    chapter_count = 0
    # Instead of relying on spine, iterate all items and look for HTML content
    for item in book.items:
        # Check if this is HTML/XHTML content
        if item.media_type in ('application/xhtml+xml', 'text/html'):
            chapter_count += 1
            chapter_title = item.title or f"Chapter {chapter_count}"

            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text_content = soup.get_text().strip()

            if text_content:
                latex_content.append(r"\chapter{" + chapter_title.replace("_", " ") + "}")
                latex_content.append(text_content.replace("\n", "\n\n"))
            else:
                print(f"Warning: Chapter '{chapter_title}' is empty.")

    if chapter_count == 0:
        print("No chapters found in the EPUB file.")
        return

    latex_content.append(r"\end{document}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(latex_content))

    print(f"LaTeX file '{output_file}' created with {chapter_count} chapters.")



# Example usage
epub_file = "austen1.epub"  # Path to your EPUB file
output_file = "output.tex"  # Desired output LaTeX file
inspect_spine(epub_file)
inspect_epub(epub_file)
epub_to_latex(epub_file, output_file)