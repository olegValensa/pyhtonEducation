
namespaces = {}

n = int(input())
# n = 4

'''
A
B : A
C : A
D : B C

A B
B D
C D
D A
'''
def add_parents(heritor, all_parents):
    print('START FUNCTION')
    if len(parents) > 0:
        print('all_parents:', all_parents)
        for y in all_parents:
            print('y:', y)
            print('namespase:', heritor, namespaces[heritor])#.extend(y)
            if y in namespaces:
                print('Y in namespaces')
                namespaces[heritor].extend(namespaces[y])
                add_parents(heritor, namespaces[y])
            else:
                print('Y NOT in namespaces')
                namespaces[y] = []
    print('STOP FUNCTION')

for command in range(n):
    parents = []
    c = input()
    if ':' in c:
        class_heritor, temp = c.split(' : ')
        parents = temp.split()
    else:
        class_heritor = c
    namespaces[class_heritor] = parents
    print('before function:', class_heritor, parents)
    add_parents(class_heritor, parents)
    print(namespaces)


def get_namespase(parent, heritor):
    if parent == heritor:
        return 'Yes'
    elif parent in namespaces[heritor]:
        return 'Yes'
    else:
        return

#namespaces = {'D': ['B', 'C'], 'C ': ['A'], 'A': [], 'B': ['A']}

m = int(input())
# m = 4
for command in range(m):
    parent, class_heritor = input().split()
    if class_heritor not in namespaces:
        print('No')
    elif parent in namespaces[class_heritor]:
        print('Yes')
    elif parent == class_heritor:
        print('Yes')
    elif len(namespaces[class_heritor]) == 0:
        print('No')
    else:
        print('No')