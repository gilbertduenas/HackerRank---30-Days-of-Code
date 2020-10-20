# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
b = bin(n)[2:].split('0')
print(len(max(b)))
