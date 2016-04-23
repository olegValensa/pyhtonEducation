import sys

s = set()
keys = {}
categories = {}

def addToCategories(s):
    for cat in s:
        if cat in categories:
            categories[cat] = categories[cat] + 1
        else:
            categories[cat] = 1

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if key not in keys:
        keys.clear()
        addToCategories(s)
        s.clear()
        keys[key] = 1
        s.add(value)
    else:
        s.add(value)
addToCategories(s)
for c in categories:
    print(str(c) + '\t' + str(categories[c]))

