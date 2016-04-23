n = int(input())#5
x = 1

destination = ['R', 'D', 'L', 'U']
dest = 0
d = destination[dest]

a = [[0 for j in range(n)] for i in range(n)]
i = j = 0
border_i = n-1
border_j = n
while x <= n * n:
    if d == 'R':
        for y in range(border_j):
            a[i][j] = x
            #print('R:', 'a', i, j, '=', x)
            x += 1
            j += 1
        j -= 1
        border_j -= 1
        #border_i -= 1
        dest = (dest + 1) % 4
        d = destination[dest]
        #print('R:', 'border j:', border_j, 'border i:', border_i, dest, d)
    if d == 'D':
        i += 1
        for y in range(border_i):
            a[i][j] = x
            #print('D:', 'a', i, j, '=', x)
            x += 1
            i += 1
        i -= 1
        border_i -= 1
        dest = (dest + 1) % 4
        d = destination[dest]
        #print('D:', 'border j:', border_j, 'border i:', border_i, dest, d)
    if d == 'L':
        j -= 1
        for y in range(border_j):
            a[i][j] = x
            #print('L:', 'a', i, j, '=', x)
            x += 1
            j -= 1
        j += 1
        border_j -= 1
        dest = (dest + 1) % 4
        d = destination[dest]
        #print('L:', 'border j:', border_j, 'border i:', border_i, dest, d)
    if d == 'U':
        i -= 1
        for y in range(border_i):
            a[i][j] = x
            #print('U:', 'a', i, j, '=', x)
            x += 1
            i -= 1
        i += 1
        j += 1
        border_i -= 1
        dest = (dest + 1) % 4
        d = destination[dest]
        #print('U:', 'border j:', border_j, 'border i:', border_i, dest, d)

for z in range(len(a)):
    for t in range(len(a[z])):
        print(a[z][t], end=' ')
    print()

