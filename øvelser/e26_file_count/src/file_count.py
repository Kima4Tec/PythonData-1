#!/usr/bin/env python3

import sys
def file_count(filename):
        with open(filename, 'r') as f:
            content = f.read()
            lines = content.splitlines()
            words = content.split()
            chars = len(content)        
            return len(lines), len(words), chars

def main():
        for filename in sys.argv[1:]:
            lines, words, chars = file_count(filename)
            print(f"{lines}\t{words}\t{chars}\t{filename}")

if __name__ == "__main__":
    main()
