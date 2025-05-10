#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    # Call the functions from here
    a=8
    b=4
    print(f"Hypotenusen, hvis a = {a} og b = {b}: {triangle.hypothenuse(a,b)}")
    print(f"Trekantens areal er: {triangle.area(a,b)}")

    # d={"Forfatter:": triangle.__author__}
    # for key, value in d.items:
    #     print(key,value)

if __name__ == "__main__":
    main()
