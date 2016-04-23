#a = [int(i) for i in input().split()]
a = [1]
i = 1
a.sort()
for c in a[i:]:
    if i < 2:
        if c == a[i-1]:
            print(c, end=' ')
    elif c == a[i-1] and c != a[i-2]:
        print(c, end=' ')
    i += 1

