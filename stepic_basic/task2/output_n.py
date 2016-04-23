a = int(input())
b = 0
c = 0
for i in range(a):
    b += 1
    for j in range(b):
        print(b, end=' ')
        c += 1
        if c == a:
            break
    if c == a:
        break