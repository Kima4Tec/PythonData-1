def detect_ranges(L):
    i = 0
    sorted_list=sorted(L)
    new_list = []

    while i < len(sorted_list): 
        start = sorted_list[i]
        end = start
        while i < len(sorted_list)-1 and sorted_list[i+1] == sorted_list[i]+1:
            i += 1
            end=sorted_list[i]
        if end != start:
                new_list.append((start, end+1))
        else:
            new_list.append(start)
        i += 1
    return new_list

def main():
    L=[2,5,4,8,12,6,7,10,13]
    print(L)
    print(detect_ranges(L))

if __name__ == "__main__":
    main()