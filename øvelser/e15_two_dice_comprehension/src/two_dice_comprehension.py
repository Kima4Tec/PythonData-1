#!/usr/bin/env python3

def main():
            d=[(i, j) 
               for i in range(1,7) 
               for j in range(1,7)
               if i + j == 5]
            for e in d:
                print(e)

if __name__ == "__main__":
    main()
