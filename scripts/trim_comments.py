"""Tiny CLI for printing text files without empty lines and comments.

This is useful for reducing the mplstyle filese to the relevant lines,
e.g., for the documentation.
"""


import sys


def trim_comments(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if not line.lstrip().startswith('#') and line.strip():
                print(line, end='')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)
    trim_comments(sys.argv[1])