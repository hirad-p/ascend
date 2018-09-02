#!/bin/python3

# From https://www.hackerrank.com/challenges/alternating-characters``

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0 # count of skips   
    p = ""    # previous letter encountered
    for c in s:
        if c != p: 
            p = c
        else:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
