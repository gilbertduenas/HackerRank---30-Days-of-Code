# https://www.hackerrank.com/challenges/30-nested-logic/problem

d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))

if d1[2] > d2[2]:
    print(10000)

elif d1[2] == d2[2] and d1[1] > d2[1]:
    print((d1[1]-d2[1]) * 500)

elif d1[2] == d2[2] and d1[1] == d2[1] and d1[0] > d2[0]:
    print((d1[0]-d2[0]) * 15)

else:
    print(0)

    
    
