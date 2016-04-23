a = []
s = input()
while s != 'end':
    a.append([int(j) for j in s.split()])
    s = input()
len_a = len(a)
for i in range(len_a):
    len_i = len(a[i])
    for j in range(len_i):
        print(a[i-1][j] + a[(i+1)%len_a][j] + a[i][j-1] + a[i][(j+1)%len_i], end=' ')
    print()


