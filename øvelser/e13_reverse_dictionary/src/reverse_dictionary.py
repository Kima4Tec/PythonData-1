#!/usr/bin/env python3

def reverse_dictionary(d):
    res={}

    for engWords, finWords in d.items():
        for finWord in finWords:
                if finWord in res:
                    res[finWord] += [engWords]
                else:
                     res[finWord]= [engWords]
    return res

def main():
   d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}

   print(reverse_dictionary(d))


if __name__ == "__main__":
    main()



d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
reverse_dictionary(d)
{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}
