#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    L = []
    with open(filename, "r") as f:
        for line in f:
            p = r"^\s*(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.*\S)\s*$"
            match = re.match(p, line)
            if match:
                r, g, b, name = match.groups()
                L.append(f"{r}\t{g}\t{b}\t{name}")
    return L


def main():
        filename=r"C:\Users\kim28\source\repos\Python\SorenPy\PythonData-1\øvelser\e23_red_green_blue\src\rgb.txt"
        for line in red_green_blue(filename):
                print(line)


if __name__ == "__main__":
    main()
