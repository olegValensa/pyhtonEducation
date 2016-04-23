import sys

for line in sys.stdin:
    tupples = {}
    for word in line.strip().split(" "):
        if word not in tupples:
            tupples[word] = 1
        else:
            tupples[word] = tupples[word] + 1
    for t in tupples:
        print(str(t) + '\t' + str(tupples[t]))

