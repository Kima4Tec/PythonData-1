#!/usr/bin/env python3

import math


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle":
            b = float(input("Give base of the triangle: "))
            h = float(input("Give height of the triangle: "))
            print(f"The area is {triangle(b,h):.6f}")
        elif shape == "rectangle":
            w = float(input("Give width of the rectangle: "))
            h = float(input("Give height of the rectangle: "))
            print(f"The area is {rectangle(w,h):.6f}")
        elif shape == "circle":
            r = float(input("Give radius of the circle: "))
            print(f"The area is {circle(r):.6f}")
        else:
            print('Unknown shape!')
            continue
            
def triangle(b,h):
    return (b*h)/2


def rectangle(w, h):
    return w * h
    

def circle(r):
    return math.pi * r * r

if __name__ == "__main__":
    main()
