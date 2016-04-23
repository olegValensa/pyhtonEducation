import sys

tupples = {}

for line in sys.stdin:
    key, value = line.strip().split('\t')

    if key not in tupples:
        if len(tupples) > 0:
            for a, b in tupples.items() :
                print (str(a)+ '\t' + str(int(b[0]/b[1])))
            tupples.clear()
        tupples[key] = (int(value), 1)
    else:
        tupples[key] = (tupples[key][0] + int(value), tupples[key][1] + 1)

for a, b in tupples.items() :
    print (str(a)+ '\t' + str(int(b[0]/b[1])))
