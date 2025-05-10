#!/usr/bin/env python3

def find_matching(L, pattern):
    res = []
    for i, words in enumerate(L):
            if pattern in words:
                 res.append(i)
    return res

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
