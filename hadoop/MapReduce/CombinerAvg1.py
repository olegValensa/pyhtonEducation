import sys

tupples = {}

for line in sys.stdin:
    key, value = line.strip().split('\t')
    seconds, one = value.strip().split(';')

    if key not in tupples:
        if len(tupples) > 0:
            for a, b in tupples.items() :
                print (str(a)+ '\t' + str(b[0]) + ';' + str(b[1]))
            tupples.clear()
        tupples[key] = (int(seconds), 1)
    else:
        sum = tupples[key][0] + int(seconds)
        count = tupples[key][1] + 1
        tupples[key] = (sum, count)

for a, b in tupples.items() :
    print (str(a)+ '\t' + str(b[0]) + ';' + str(b[1]))
