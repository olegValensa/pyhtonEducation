namespaces = {}

n = int(input())
# n = 6

for command in range(n):
    parents = []
    c = input()
    if ':' in c:
        class_heritor, temp = c.split(' : ')
        parents = temp.split()
    else:
        class_heritor = c
    namespaces[class_heritor] = parents
    # print(namespaces)

# namespaces = {'A': [], 'C': ['B', 'A'], 'G': [], 'B': ['A'], 'D': ['G'], 'E': ['C', 'D', 'B', 'A', 'A', 'G', 'A']}

def add_parents(class_with_parents, parents):
    for x in parents:
        # print(x, ':', namespaces[x])
        namespaces[class_with_parents].extend(namespaces[x])
        if len(namespaces[x]) > 0:
            add_parents(class_with_parents, namespaces[x])

def is_parent(A, B):
    if A == B:
        return 'Yes'
    elif B in namespaces[A]:
        return 'Yes'
    else:
        return 'No'

for y in namespaces:
    # print('y in loop:', y)
    add_parents(y, namespaces[y])

# print(namespaces)

m = int(input())
# m = 3
for command in range(m):
    parent, class_heritor = input().split()
    print(is_parent(class_heritor, parent))