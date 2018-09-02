#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    word_map = {}
    for word in magazine:
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1
    
    
    for word in note:
        if  word not in word_map or word_map[word] < 1:
            print("No")
            return
        else: 
            word_map[word] -= 1
    
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
