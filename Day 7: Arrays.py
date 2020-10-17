# https://www.hackerrank.com/challenges/30-arrays/problem

n = int(input())

def string_loop(s):
    e = []
    o = []

    for i in range(len(s)):
        if i%2 == 0:
            e.append(s[i])
        else:
            o.append(s[i])

    E = ''.join(e)
    O = ''.join(o)

    return f'{E} {O}'

for i in range(n):
    print(string_loop(input()))
