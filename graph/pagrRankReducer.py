import sys

keySum = 0.0
keyOut = None
lastKey = None

for row in sys.stdin:
    key, totalWeigth, outs = row.strip().split('\t')
    if lastKey and lastKey != key:
        keySum = 0.02 + 0.9 * keySum
        print(lastKey + '\t' + str(format(keySum, '.3f') + '\t' + keyOut))
        if outs == '{}':
            keySum = float(totalWeigth)
        else:
            keySum = 0.0
        keyOut = outs
        lastKey = key
    elif lastKey and lastKey == key:
        if outs == '{}':
            keySum += float(totalWeigth)
        else:
            keyOut = outs
    else:
        if outs == '{}':
            keySum = float(totalWeigth)
        keyOut = outs
        lastKey = key
if lastKey:
    keySum = 0.02 + 0.9 * keySum
    print(lastKey + '\t' + str(format(keySum, '.3f') + '\t' + keyOut))
