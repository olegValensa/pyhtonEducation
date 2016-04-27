from random import random

lst = [1, 2, 3, 4, 5, 6, 7]

'''
for i in lst:
    print(i)

print('----NEXT----')

it = iter(lst)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
''
class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

for x in RandomIterator(5):
    print(x)
'''

class DoubleElementsIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        return DoubleElementsIterator(self)

for pair in MyList([1, 2, 3, 4]):
    print(pair)
