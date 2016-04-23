def swap(i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(A, l, r):
    print('------ A, l, r', A, l, r)
    x = A[l]
    print('x:', x)
    j = l
    print('j = l', j)
    for i in range(l+1, r):
        print('A[',i, '] =', A[i])
        if A[i] < x:
            j = j + 1
            swap(i, j)
            print('changed A:', A)
    if A[l] != A[j]:
        swap(l, j)
    return j+1


def quickSort(A, l, r):
    if l+1 >= r:
        return
    m = partition(A, l, r)
    quickSort(A, l, m)
    quickSort(A, m, r)



A = [7, 6, 5, 4, 3, 2, 1]#[6, 3, 2, 2, 9, 4, 1, 0, 5] #
quickSort(A, 0, len(A))
print(A)
