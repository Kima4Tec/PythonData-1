#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    L=[]
    with open(filename, "r") as f:
        for line in f:
            p= r"(\d+) (\w{3}) +(\d+) +(\d{1,2}):(\d{1,2})(.*)$"
            liste= re.findall(p, line)
            liste = liste[0]
            # print(liste)
            L.append((int(liste[0]), liste[1], int(liste[3]),int(liste[4]),liste[5]))

    return L

def main():
    filename=r"C:\Users\kim28\source\repos\Python\SorenPy\PythonData-1\øvelser\e22_file_listing\src\listing.txt"
    print(*file_listing(filename), sep='\n')

if __name__ == "__main__":
    main()
