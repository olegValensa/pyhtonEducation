def gcd(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b % a, a)
    '''elif a >= b:
        return gcd(a % b, b)
    elif a < b:
        return gcd(a, b % a)'''

a, b = (int(x) for x in input().split())
print(gcd(a, b))
