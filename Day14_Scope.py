class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        max_element = max(self.__elements)
        min_element = min(self.__elements)
        self.maximumDifference = abs(max_element - min_element)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
