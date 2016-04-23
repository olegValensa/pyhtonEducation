import sys

def Dijkstra(W, start):
    INF = 10 ** 10
    D = [INF] * N
    D[start-1] = 0
    Colored = [False] * N
    while True:
        min_dist = INF
        for i in range(N):
            if not Colored[i] and D[i] < min_dist:
                min_dist = D[i]
                min_vertex = i
        if min_dist == INF:
            break
        i = min_vertex
        Colored[i] = True
        for j in range(N):
            if i+1 in W and j+1 in W[i+1]:
                if D[i] + W[i+1][j+1] < D[j]:
                    D[j] = D[i] + W[i+1][j+1]
    return D

def Distance(D, element):
    if D[element-1] == INF:
        return -1
    else:
        return D[element-1]



W = {}
start = 0
count = 0
N = 0
numberOfEdges = 0
dest = 0
INF = 10 ** 10

for row in sys.stdin:
    if count == 0:
        N, numberOfEdges = [int(i) for i in row.split()] #row.split()
    elif count > numberOfEdges:
        start, dest = [int(i) for i in row.split()]
    else:
        out, dest, weight = [int(i) for i in row.split()]
        if out in W:
           if dest not in W[out]:
               W[out][dest] = weight
        else:
            W[out] = {dest:weight}
        vertex = row.split()[1]
    count += 1

print(Distance(Dijkstra(W, start), dest))
