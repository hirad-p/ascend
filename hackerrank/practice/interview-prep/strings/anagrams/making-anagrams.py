#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # make a count map that has each character in both strings 
    # if the character appears in a increment the count
    # if the character appears in b decrement the count
    counts = {}
    for c in a:
        if c in counts:
            counts[c] += 1
        else: 
            counts[c] = 1

    for c in b:
        if c in counts:
            counts[c] -= 1
        else: 
            counts[c] = -1
        
    # go through the count items and find the total (abs)
    count = 0
    for value in counts.values():
        count += abs(value)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
