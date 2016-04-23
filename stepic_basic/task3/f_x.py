def f(x):
    return x*2+1

n = int(input())
dic = {}
lst = []
c = 0
for a in range(n):
    x = int(input())
    lst.append(x)
    if (x not in dic):
        dic[x] = f(x)
for i in lst:
    print(dic[i])
