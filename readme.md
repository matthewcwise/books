# Gutenberg to LaTeX Converter

## Overview
This tool converts a raw Project Gutenberg `.txt` file into a print-ready LaTeX `.tex` file. It removes extraneous licensing text, extracts the title and author, formats chapters, and prepares a LaTeX document suitable for generating a PDF.

## Usage
1. Place `template.tex` and `convert.py` in the same directory.
2. Run:
   ```bash
   python convert.py input.txt