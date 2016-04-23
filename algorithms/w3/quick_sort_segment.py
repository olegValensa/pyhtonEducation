def quickSearchBeg(A, point, l, r):
    #print('------- A:', A)
    if l >= r:
        return
    m = (l + r) // 2
    #print("l, r, m", l, r, m)
    #print('A[m] =', A[m])
    #print('A[m-1] =', A[m-1])
    if A[m-1] <= point and A[m] > point:
        return m
    elif A[m] <= point:
        return quickSearch(A, point, m+1, r)
    elif A[m] > point:
        return quickSearch(A, point, l, m)

def quickSearchEnd(A, point, l, r):
    #print('------- A:', A)
    if l >= r:
        return
    m = (l + r) // 2
    #print("l, r, m", l, r, m)
    #print('A[m] =', A[m])
    #print('A[m-1] =', A[m-1])
    if A[m-1] < point and A[m] > point:
        return m
    elif A[m-1] == point and A[m] > point:
        i = 0
        while A[m-1-i] == point:
            i += 1
        return m-1
    elif A[m] <= point:
        return quickSearch(A, point, m+1, r)
    elif A[m] > point:
        return quickSearch(A, point, l, m)


def quickSearchOpt(A, point, l, r, marker):
    if A[0] > point:
        return 0
    elif A[0] == A[(len(A)-1)] and len(A) > 1:
        if A[0] >= point:
            return len(A)
        else:
            return 0
    elif A[len(A)-1] < point:
        return len(A)
    elif A[len(A)-1] == point:
        i = len(A) - 1
        while A[i] == point:
            i -= 1
        return i+1
    else:
        if marker == 'B':
            return quickSearchBeg(A, point, l, r)
        elif marker == 'E':
            return quickSearchEnd(A, point, l, r)



n, m = (int(x) for x in input().split())
Start = []
End = []
for t in range(n):
    a, b = (int(x) for x in input().split())
    Start.append(a)
    End.append(b)
points = [int(i) for i in input().split()]

Start.sort()
End.sort()

for point in points:
    #print(quickSearchOpt(Start, point, 0, n) - quickSearchOpt(End, point, 0, n), end=' ')
    print('Start', quickSearchOpt(Start, point, 0, n, 'B'))
    print('End', quickSearchOpt(End, point, 0, n, 'E'))