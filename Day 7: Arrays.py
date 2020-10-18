# https://www.hackerrank.com/challenges/30-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = input()

    arr = list(map(str, input().rstrip().split()))
    
    print(' '.join(reversed(arr)))
