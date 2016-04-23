a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b >= a and d >= c:
    for i in range(a-1, b+1):
        if i == a-1:
            print('\t', end='')
        else:
            print(str(i) + '\t', end='')
        for j in range (c, d+1):
            if i == a-1:
               print(str(j) + '\t', end='')
            else:
                print(str(j*i) + '\t', end='')
            if j == d:
                print()