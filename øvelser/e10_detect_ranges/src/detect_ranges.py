#!/usr/bin/env python3

def detect_ranges(L):
    i = 0
    SortedList = sorted(L)
    NewList = []
    
    while i < len(SortedList):
        start = SortedList[i]
        end = start
        while i < len(SortedList)-1 and SortedList[i+1] == SortedList[i]+1:
            i+=1
            end = SortedList[i]
        if start != end:
            NewList.append((start, end + 1))
        else:
            NewList.append(start)
        i += 1     
    return NewList

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
