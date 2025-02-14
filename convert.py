import sys
import re

def extract_metadata(lines):
    """
    Extracts the Title and Author from the provided lines.
    """
    title = "Unknown Title"
    author = "Unknown Author"
    for line in lines:
        line_stripped = line.strip()
        if line_stripped.lower().startswith("title:"):
            title = line_stripped[6:].strip()
        elif line_stripped.lower().startswith("author:"):
            author = line_stripped[7:].strip()
    return title, author

def clean_text(text):
    """
    Cleans and formats the text by handling italics, normalizing whitespace,
    converting quotes and dashes, and formatting bracketed notes.
    """
    # Step 1: Normalize line endings and split into lines
    lines = text.splitlines()
    
    # Step 2: Group lines into paragraphs based on blank lines
    paragraphs = []
    current_paragraph = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            current_paragraph.append(stripped_line)
        else:
            if current_paragraph:
                # Join the current paragraph's lines with spaces
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = []
    # Add the last paragraph if any
    if current_paragraph:
        paragraphs.append(' '.join(current_paragraph))
    
    # Step 3: Join paragraphs with double newlines for LaTeX
    text = '\n\n'.join(paragraphs)
    
    # Step 4: Replace underscores with \textit{}, handling multiple italics
    # This regex finds pairs of underscores surrounding any characters (non-greedy)
    # including those spanning multiple lines because the DOTALL flag is used
    italic_pattern = re.compile(r'_(.*?)_', re.DOTALL)
    text = italic_pattern.sub(r'\\textit{\1}', text)
    
    # Step 5: Normalize whitespace: replace multiple spaces with single space
    text = re.sub(r'[ \t]+', ' ', text)
    
    # Step 6: Normalize multiple blank lines to a single blank line
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    
    # Step 7: Replace dashes with LaTeX-friendly forms
    text = text.replace('---', '---')  # Ensure em-dashes are '---'
    text = text.replace('--', '---')   # Replace double-dash with triple-dash for em-dash
    
    # Step 8: Convert smart quotes to LaTeX quotes
    text = text.replace('“', '``').replace('”', "''")
    text = text.replace('‘', '`').replace('’', "'")
    
    # Step 9: Convert [Illustration: ...] or other bracketed notes into \emph{...}
    # text = re.sub(r'\[Illustration:(.*?)\]', r'\\emph{[Illustration:\1]}', text, flags=re.IGNORECASE)
    
    # Step 10: Handle footnotes if present (e.g., (Footnote: ...))
    footnote_pattern = re.compile(r'\(Footnote:\s*(.*?)\)', re.IGNORECASE)
    text = footnote_pattern.sub(r'\\footnote{\1}', text)
    
    return text

def identify_chapters(text):
    """
    Identifies chapters in the text, prints the original chapter heading and the
    corresponding LaTeX chapter name, replaces chapter headings with LaTeX \chapter{...}
    commands, and returns the modified text.
    """
    # Define patterns for different chapter headings
    chapter_patterns = [
        r'^(chapter\s+[ivxlc\d]+\.?)$',  # e.g., "CHAPTER I"
        r'^(stave\s+[ivxlc\d]+[.:]?.*)$',  # e.g., "STAVE I: MARLEY'S GHOST"
        r'^\s*preface\.?$',  # e.g., "PREFACE"
        r'^\s*introduction\.?$'  # e.g., "INTRODUCTION"
    ]

    # Combine all patterns into one regex using alternation
    combined_pattern = re.compile(
        r'(?mi)^(chapter\s+[ivxlc\d]+\.?)$|^(stave\s+[ivxlc\d]+[.:]?.*)$|^\s*preface\.?$|^\s*introduction\.?$',
        re.MULTILINE
    )

    # Find all chapter headings with their positions
    matches = list(combined_pattern.finditer(text))

    # If no chapters found, return the original text
    if not matches:
        print("No chapters found.")
        return text

    chapters = []
    for i, match in enumerate(matches):
        start = match.start()
        end = match.end()

        # Determine the title of the chapter
        chapter_title = match.group().strip()

        # Determine the LaTeX-formatted chapter name
        if chapter_title.lower().startswith("chapter"):
            # Preserve Roman numeral case
            parts = chapter_title.split()
            parts[1] = parts[1].upper()  # Assuming the second word is the Roman numeral
            latex_chapter_name = " ".join(parts)
            latex_command = f"\\chapter{{{latex_chapter_name}}}"
        elif chapter_title.lower().startswith("stave"):
            # Handle 'stave' chapters (e.g., STAVE I: MARLEY'S GHOST)
            stave_match = re.match(r'(stave\s+[ivxlc\d]+[.:]?)(.*)', chapter_title, re.IGNORECASE)
            if stave_match:
                stave_number = stave_match.group(1).title().rstrip('.').upper()  # Preserve Roman numeral case
                stave_name = stave_match.group(2).strip().title()
                latex_chapter_name = f"{stave_number}: {stave_name}"
            else:
                latex_chapter_name = chapter_title.title()
            latex_command = f"\\chapter{{{latex_chapter_name}}}"
        elif chapter_title.lower().startswith("preface"):
            latex_chapter_name = "Preface"
            latex_command = f"\\chapter*{{{latex_chapter_name}}}"
        elif chapter_title.lower().startswith("introduction"):
            latex_chapter_name = "Introduction"
            latex_command = f"\\chapter*{{{latex_chapter_name}}}"
        else:
            # Fallback for any other types
            latex_chapter_name = chapter_title.title()
            latex_command = f"\\chapter{{{latex_chapter_name}}}"

        # Print the original chapter heading and the LaTeX chapter name
        print(f"Original Chapter Heading: \"{chapter_title}\"")
        print(f"LaTeX Chapter Name: \"{latex_chapter_name}\"\n")

        # Determine the start and end of the chapter content
        if i + 1 < len(matches):
            chapter_content = text[end:matches[i + 1].start()].strip()
        else:
            chapter_content = text[end:].strip()

        # Replace the chapter heading with the LaTeX command
        chapters.append(latex_command + "\n\n" + chapter_content)

    # Join all chapters with double newlines for LaTeX
    modified_text = "\n\n".join(chapters)

    return modified_text


import re

def remove_bracketed_notes(text):
    """
    Identifies and removes or italicizes bracketed notes that are not illustrations.
    Prints each bracketed note that is being processed for transparency.
    """
    def replace_bracketed(match):
        # Extract the matched text inside brackets
        content = match.group(1)
        print(f"Processing bracketed note: [{content}]")
        # Return the LaTeX-italicized version
        return r'\emph{[' + content + ']}'
    
    # Find and replace bracketed notes, excluding those starting with 'Illustration:'
    # Instead of a broad search, ensure the bracket isn't preceded by a backslash or command.
    updated_text = re.sub(r'(?<!\\)\[(?!Illustration:)(.*?)\]', replace_bracketed, text)
    updated_text = re.sub(r'\[(?!Illustration:|h\])(.*?)\]', replace_bracketed, text)


    return updated_text
import re

def process_illustrations(text):
    """
    Detects illustrations in the text and includes their details in a LaTeX-friendly format.
    """
    return text
#     def replace_illustration(match):
#         # Extract the entire illustration content
#         illustration_content = match.group(1).strip()
#         print(f"Processing Illustration: {illustration_content}")

#         # Convert to LaTeX-friendly format, preserving content
#         return r"""\begin{figure}[h]
# \centering
# \emph{""" + illustration_content + r"""}
# \end{figure}
# """

#     # Match [Illustration: ...] blocks with multiline support
#     illustration_pattern = re.compile(r'\[Illustration:\s*(.*?)\]', re.DOTALL)
#     updated_text = illustration_pattern.sub(replace_illustration, text)
#     return updated_text


def convert_footnotes(text):
    """
    Converts footnotes in the format (Footnote: ...) to LaTeX \footnote{...}.
    """
    # Convert footnotes from (Footnote: ...) to \footnote{...}
    footnote_pattern = re.compile(r'\(Footnote:\s*(.*?)\)', re.IGNORECASE)
    text = footnote_pattern.sub(r'\\footnote{\1}', text)
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read template
    try:
        with open("template.tex", "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print("Error: 'template.tex' not found in the current directory.")
        sys.exit(1)

    # Read input file
    try:
        with open(input_file, "r", encoding="utf-8", errors="replace") as f:
            all_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Find the start and end markers
    start_index = None
    end_index = None
    for i, line in enumerate(all_lines):
        if re.search(r'^\*\*\* START OF THE PROJECT GUTENBERG EBOOK', line, re.IGNORECASE):
            start_index = i
        if re.search(r'^\*\*\* END OF THE PROJECT GUTENBERG EBOOK', line, re.IGNORECASE):
            end_index = i

    if start_index is None or end_index is None:
        print("Error: Could not find start/end markers in the input file.")
        sys.exit(1)

    # Extract text between markers
    main_text_lines = all_lines[start_index+1:end_index]

    # Extract metadata (Title, Author)
    title, author = extract_metadata(main_text_lines)

    # Remove metadata lines from main_text_lines to avoid duplication in final text
    main_text_lines = [
        l for l in main_text_lines
        if not l.strip().lower().startswith("title:")
        and not l.strip().lower().startswith("author:")
    ]

    # Join lines into a single text block for further processing
    text = "".join(main_text_lines)

    # Remove Project Gutenberg references (heuristic)
    text = re.sub(r'(Project Gutenberg|www\.gutenberg\.org)', '', text, flags=re.IGNORECASE)

    # Clean the text
    text = clean_text(text)
    text = remove_bracketed_notes(text)
    text = process_illustrations(text)
    text = identify_chapters(text)
    text = convert_footnotes(text)

    # Insert Title and Author into template
    final_tex = template.replace("<TITLE_PLACEHOLDER>", title)
    final_tex = final_tex.replace("<AUTHOR_PLACEHOLDER>", author)

    # Insert the processed text before \end{document}
    final_tex = final_tex.replace("% The main text will be inserted here by the Python script", text)

    # Write out to output.tex
    with open("output.tex", "w", encoding="utf-8") as f:
        f.write(final_tex)

    print("Conversion complete. Run pdflatex on output.tex to generate the PDF.")

if __name__ == "__main__":
    main()
