import sys
import re

lastkey = None
distance = None
outs = []

for row in sys.stdin:
    key, minDist, outVertex = row.strip().split('\t')
    if lastkey and lastkey == key:
        if minDist != 'INF':
            if distance != 'INF':
                distance = min(int(minDist), int(distance))
            else:
                distance = minDist
        if outVertex != '{}':
            outs = outVertex #[int(i) for i in re.findall(r"[\w']+", outVertex)]
    elif lastkey and lastkey != key:
        print(lastkey + '\t' + str(distance) + '\t' + outs)
        lastkey = key
        distance = minDist
        outs = outVertex # [int(i) for i in re.findall(r"[\w']+", outVertex)]
    else:
        lastkey = key
        distance = minDist
        outs = outVertex # [int(i) for i in re.findall(r"[\w']+", outVertex)]
if lastkey:
    print(lastkey + '\t' + str(distance) + '\t' + outs)