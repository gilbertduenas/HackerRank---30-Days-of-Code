# https://www.hackerrank.com/challenges/30-scope/problem

Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        max_ele = max(self.__elements)
        min_ele = min(self.__elements)

        self.maximumDifference = abs(max_ele - min_ele)
    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
