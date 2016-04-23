#a = [int(i) for i in input().split()]
l = len(a)
i = 0
s = 0
for b in a:
    if l == 1:
        print(b)
    else:
        s = a[(i+1) % l] + a[i-1]
        print(s, end=' ')
    i += 1

