import sys
import re

lastKey = None
tempOutput = []
sum = 0

for line in sys.stdin:
    key, doc, count, docCount = (re.findall(r"[\w']+", line))
    if lastKey and lastKey == key:
        tempOutput.append(str(key + '#' + doc + '\t' + count))
        sum += int(docCount)
    elif lastKey and lastKey != key:
        for row in tempOutput:
            print(row + '\t' + str(sum))
        tempOutput = []
        tempOutput.append(str(key + '#' + doc + '\t' + count))
        lastKey = key
        sum = 1
    else:
        lastKey = key
        tempOutput.append(str(key + '#' + doc + '\t' + count))
        sum += int(docCount)
if lastKey:
    for row in tempOutput:
        print(row + '\t' + str(sum))
