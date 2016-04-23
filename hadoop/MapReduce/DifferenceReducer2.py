import sys

lastKey = None
groups = {}
bunch = set('A')

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        if groups[lastKey] == bunch:
            print(lastKey)
        groups.pop(lastKey)
        (lastKey, groups[key]) = (key, set(value))
    elif lastKey and lastKey == key:
        groups[key].add(value)
    else:
        lastKey = key
        groups[key] = set(value)
if lastKey and groups[lastKey] == bunch:
    print (lastKey)