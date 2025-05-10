#!/usr/bin/env python3

def transform(s1, s2):
    L=[a*b for a,b in (zip(map(int, s1.split()),map(int, s2.split())))]
    L1 = list(map(lambda x: x[0] * x[1], zip(map(int, s1.split()), map(int, s2.split()))))
    L2=[]
    tal1=list(map(int, s1.split()))
    tal2=list(map(int, s2.split()))
    for a,b in zip(tal1,tal2):
        L2.append(a*b)
    return L,L1,L2
    

def main():
    print(transform("1 5 3" , "2 6 -1"))

if __name__ == "__main__":
    main()