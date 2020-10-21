# https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    m = []
    max = -63

    for _ in range(6):
        m.append(list(map(int, input().rstrip().split())))

    for i in range(len(m)-2):
        for j in range(len(m)-2):
            check = m[i][j]+m[i][j+1]+m[i][j+2] + m[i+1][j+1] + m[i+2][j]+m[i+2][j+1]+m[i+2][j+2]

            if check > max:
                max = check
    
    print(max)
