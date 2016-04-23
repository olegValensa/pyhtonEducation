import sys
import re

for row in sys.stdin:
    key, minDist, outs = row.strip().split('\t')
    outVertex = [int(i) for i in re.findall(r"[\w']+", outs)]
    print(key + '\t' + minDist + '\t' + outs)
    for v in outVertex:
        if minDist == 'INF':
            print(str(v) + '\t' + minDist + '\t' + str({}))
        else:
            print(str(v) + '\t' + str(int(minDist)+1) + '\t' + str({}))

