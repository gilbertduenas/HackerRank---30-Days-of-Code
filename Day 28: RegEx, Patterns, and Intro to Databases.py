# https://www.hackerrank.com/challenges/30-regex-patterns/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    regex = r"([a-z]+) ([a-z]+?.{0,20})(@gmail.com{0,50})"
    subst = []
    
    for N_itr in range(N):
        result = re.findall(regex, input())

        for i in result:
            subst.append(i[0])

    for i in sorted(subst):
        print(i)

