#!/usr/bin/python3

import sys
import os

def main():
    #Check the number of arguments
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

            # If everything is okay, print nothing and exit with status 0
            sys.exit(0)
            if __name__ == "__main__":
                main()
