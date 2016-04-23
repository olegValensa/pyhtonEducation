class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError(str(x) + " is negative")

a = PositiveList([1, 2])
print(a)
a.append(4)
print(a)
a.append(0)
print(a)
a.append(-1)
