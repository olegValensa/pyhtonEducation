import sys

lastKey = None
groups = {}

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        if len(groups[lastKey]) == 1:
            print(lastKey)
        groups.pop(lastKey)
        (lastKey, groups[key]) = (key, set(value))
    elif lastKey and lastKey == key:
        groups[key].add(value)
    else:
        lastKey = key
        groups[key] = set(value)
if lastKey and len(groups[lastKey]) == 1:
    print (lastKey)
