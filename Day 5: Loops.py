# https://www.hackerrank.com/challenges/30-loops/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

for i in range(1, 11):
    p = n*i
    print(f'{n} x {i} = {p}')
