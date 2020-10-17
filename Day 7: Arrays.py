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

# Or I could do this to replace lines 6 to 18.
#     for i in range(n):
#         return f'{s[::2]} {s[1::2]}'

for i in range(n):
    print(string_loop(input()))
