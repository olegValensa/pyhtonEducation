def countInversions(add):
    global  itering
    itering += add

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                #print("1 CASE: i, j, left[i], right[j]", i, j, lefthalf, righthalf)
                countInversions(len(lefthalf) - i)
                j=j+1
            k=k+1

        '''if (i - 1) < len(lefthalf):
            add = len(lefthalf) - i - 1
            countInversions(add * len(righthalf))'''
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            #if len(righthalf) > 1:
              #  countInversions()
            #print("2 CASE: i, j, left[i]", i, j, lefthalf)
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            #countInversions()
            j=j+1
            k=k+1
    #print("Merging ",alist)

#n = int(input())
#A = [int(i) for i in input().split()]
#A = []
#for x in range(n):
#print(A)

A = [1, 2, 3, 5, 4]#[7, 6, 5, 4, 3, 2, 1]#[2, 3, 9, 2, 9] #
#mergeSort(A)
itering = 0
mergeSort(A)
print(itering)
#print(A)