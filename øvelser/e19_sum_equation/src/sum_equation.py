#!/usr/bin/env python3

def sum_equation(L: list):
    if len(L) == 0:
        return "0 = 0"
    
    s1 =' + '.join(map(str,L))
    return f"{s1} = {sum(L)}"
    return s1 + ' = ' + str(s)

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()


# Write a function `sum_equation` which takes a list of positive integers as parameters 
# and returns a string with an equation of the sum of the elements.

# Example:
# `sum_equation([1,5,7])`
# returns
# `"1 + 5 + 7 = 13"`
# Observe, the spaces should be exactly as shown above. For an empty list the function should return the string "0 = 0".