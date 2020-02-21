#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if(len(s) % 2 == 1):
        return -1
    else:
        half = int(len(s)/2)
        s_1 = s[0:half]
        s_2 = s[half:]
        print(s_1+ " " + s_2)
        if sorted(s_1) == sorted(s_2):
            return 0
        else:
            count = [0,0]
            for i in range (len(s_1)):
                if s_1[i] not in s_2:
                    count[0] += 1
            for i in range(len(s_2)):
                if s_2[i] not in s_1:
                    count[1] += 1
            return max(count)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for i in range(q):
        s = input()

        result = anagram(s)
        print(result)

