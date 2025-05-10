#!/usr/bin/env python3

def distinct_characters(L):
    d={}
    for i in L:
        d[i]=len(set(i))
    # len(set(d)
    return d

    # while i < len(L):

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))
# output: { "check" : 4, "look" : 3, "try" : 3, "pop" : 2}
if __name__ == "__main__":
    main()
