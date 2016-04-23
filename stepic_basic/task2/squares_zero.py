#a = [int(i) for i in input().split()]
#a = [1,-3,5,-6,-10,13,4,-8]
s = 0
ss = 0
while True:
    a = int(input())
    s += a
    ss += a*a
    if s == 0:
        break
print(ss)