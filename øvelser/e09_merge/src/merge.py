#!/usr/bin/env python3

def merge(L1, L2):
    i, j = 0, 0
    L = []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1

    L.extend(L1[i:])
    L.extend(L2[j:])

    return L



def main():
    L1=[1,3,8,12,27]
    L2=[2,4,6,9]
    result = merge(L1,L2)
    print(result)

if __name__ == "__main__":
    main()
