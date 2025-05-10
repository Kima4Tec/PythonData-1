#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    tallerne = []
    with open(filename, "r") as f:
        for line in f:
            try:
                tallerne.append(float(line))
            except ValueError:
                pass
    n=len(tallerne)
    total=sum(tallerne)
    avg = total/n
    std = statistics.stdev(tallerne)

    return (total,avg,std)


def main():
    for filename in sys.argv[1:]:
        total, avg, std = summary(filename)
        print(f"File: {filename} Sum: {total:.6f} Average: {avg:.6f} Stddev: {std:.6f}")

if __name__ == "__main__":
    main()
