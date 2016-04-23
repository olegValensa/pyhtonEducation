import sys

(lastkey, sum) = (None, 0)

tupples = {}

for line in sys.stdin:
    (key, value) = line.strip().split('\t')
    if key not in tupples:
        print(lastkey + '\t' + str(sum))
        tupples[key] = (int(value), 1)
    else:
        tupples[key] = (tupples[key][0] + int(value), tupples[key][1] + 1)
for t in tupples:
    print(str(t) + '\t' + str(tupples[t]))
