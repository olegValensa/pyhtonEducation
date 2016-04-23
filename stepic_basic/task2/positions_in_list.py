#lst = [int(i) for i in input().split()]
lst = [5, 8, 2, 7, 8, 8, 2, 4]
x = 10#int(input())
a = 0
b = False
for i in lst:
    if i == x:
        print(a, end=' ')
        b = True
    a += 1
if b == False:
    print('???????????')
