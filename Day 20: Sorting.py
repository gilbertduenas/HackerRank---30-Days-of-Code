# https://www.hackerrank.com/challenges/30-sorting/problem

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def bubble(a):
    count = 0
    for num in range(len(a)-1, 0, -1):
        for i in range(num):
            if a[i] > a[i+1]:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
                count +=1
    return count

print "Array is sorted in {} swaps.".format(bubble(a))
print "First Element: {}".format(a[0])
print "Last Element: {}".format(a[-1])
