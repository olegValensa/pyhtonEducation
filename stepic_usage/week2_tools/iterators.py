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


def random_generator(k):
    for i in range(k):
        yield random()

gen = random_generator(3)
print(type(gen))


x = [-2, -1, 0, 1, 2]
y = [i * i for i in x if i > 0]
print(y)

z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)

z1 = ((x, y) for x in range(3) for y in range(3) if y >= x)
print(z1)
print(next(z1))
print(next(z1))
print(next(z1))
'''

a = [i + 1 for i in range(4)]
print(a)
b = [i for i in range(4)]
print(b)
c = [i for i in range(5)][1:]
print(c)
d = list(i + 1 for i in range(4))
print(d)