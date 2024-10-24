#!/usr/bin/python3

import sys
import os
import re
import hashlib

def md5_hash(text):
    """Return the MD5 hash of the input string in lowercase."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def remove_case_insensitive_c(text):
    """Remove all 'c' characters from the input string, case insensitive."""
    return re.sub(r'(?i)c', '', text)

def parse_bold_and_italic(text):
    """Convert Markdown bold and italic syntax to HTML."""
    # Existing parsing for bold and italic
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # **text** to <b>text</b>
    text = re.sub(r'__(.*?)__', r'<em>\1</em>', text)  # __text__ to <em>text</em>
    return text

def convert_markdown_to_html(markdown_file, output_file):
    """Convert various Markdown syntaxes in a markdown file to HTML and save to output file."""
    
    with open(markdown_file, 'r') as md_file, open(output_file, 'w') as html_file:
        paragraphs = []  # Store paragraph lines
        
        for line in md_file:
            stripped_line = line.strip()

            # If line is blank, it indicates the end of a paragraph
            if not stripped_line:
                if paragraphs:
                    paragraph = " ".join(paragraphs)  # Join paragraph lines
                    paragraph = parse_bold_and_italic(paragraph)  # Apply parsing for bold/italic
                    html_file.write(f"<p>{paragraph}</p>\n")
                    pragraphs = []  # Clear the paragraph buffer
                    continue
                
                # Handle Markdown specific formatting
                if stripped_line.startswith('[[') and stripped_line.endswith(']]'):
                    # Convert to MD5
                    content = stripped_line[2:-2]  # Extract the content
                    md5_result = md5_hash(content)
                    html_file.write(f"<p>{md5_result}</p>\n")
                    continue
                elif stripped_line.startswith('((') and stripped_line.endswith('))'):
                    # Remove 'c' from content
                    content = stripped_line[2:-2]  # Extract the content
                    no_c_content = remove_case_insensitive_c(content)
                    html_file.write(f"<p>{no_c_content}</p>\n")
                    continue

                    # If this is plain text or other paragraphs, treat it as part of the paragraph
                    paragraphs.append(stripped_line)
                    
                    # Write any remaining paragraphs at the end of the file
                    if paragraphs:
                        paragraph = " ".join(paragraphs)  # Join paragraph lines
                        paragraph = parse_bold_and_italic(paragraph)  # Apply parsing for bold/italic
                        html_file.write(f"<p>{paragraph}</p>\n")

def main():
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

        # Assign the arguments to variables
        markdown_file = sys.argv[1]
        output_file = sys.argv[2]

        # Check if the Markdown file exists
        if not os.path.isfile(markdown_file):
             print(f"Missing {markdown_file}", file=sys.stderr)
             sys.exit(1)

        # Convert Markdown to HTML
        convert_markdown_to_html(markdown_file, output_file)

        # If everything is okay, print nothing and exit with status 0
        sys.exit(0)

    if __name__ == "__main__":
        main()
