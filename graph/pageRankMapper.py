import sys
import re

for row in sys.stdin:
    print(row.strip())
    key, totalWeigth, outs = row.strip().split('\t')
    outVertex = [int(i) for i in re.findall(r"[\w]+", outs)]
    outNumber = len(outVertex)
    outWeigth = format(float(totalWeigth)/outNumber, '.3f')
    for v in outVertex:
        print(str(v) + '\t' + str(outWeigth) + '\t{}')