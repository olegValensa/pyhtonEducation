from random import random
import math
import itertools


'''
def primes(N):
    """?????????? ??? ??????? ?? 2 ?? N"""
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))
    return sieve
print(primes(10))
'''

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def primes():
    i = 2
    while True:
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            yield i
        i += 1

def is_prime(x):
    if x % 2 and x > 2:
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
    elif x != 2:
        return False
    return True

'''
    d, n = 2, 2
    while True:
        while n % d != 0:
            d += 1
            print(d)
        yield d
    '''
print(IsPrime(4))
print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
