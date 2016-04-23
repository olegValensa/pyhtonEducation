a, b = (int(i) for i in input().split())
s = c = 0
while a % 3 != 0:
    a = a + 1
for i in range(a, b+1, 3):
    s += i
    c += 1
print(s / c)


