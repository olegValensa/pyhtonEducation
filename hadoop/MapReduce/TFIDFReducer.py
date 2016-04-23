import sys
import re

lastKey = None
lastDoc = None
sum = 0

for line in sys.stdin:
    word, doc, count = (re.findall(r"[\w']+", line))
    if lastKey and lastKey == word:
        if lastDoc == doc:
            sum += int(count)
        else:
            print(lastKey + '\t' + lastDoc + '\t' + str(sum))
            lastDoc = doc
            sum = 1
    elif lastKey and lastKey != word:
        print(lastKey + '\t' + lastDoc + '\t' + str(sum))
        lastKey, lastDoc = word, doc
        sum = 1
    else:
        lastKey, lastDoc = word, doc
        sum = 1
if lastKey:
    print(lastKey + '\t' + lastDoc + '\t' + str(sum))
