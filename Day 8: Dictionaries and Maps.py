# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())

d = {}

for i in range(n):
    k, v = map(str, input().split())

    d[k] = v

for j in range(n):
    try:
        s = input()

        if s in d.keys():
            print(f'{s}={d[s]}')
        else:
            print('Not found')
            
    except:
        break 
