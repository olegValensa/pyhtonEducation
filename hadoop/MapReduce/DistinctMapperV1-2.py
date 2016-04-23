import sys

keys = []

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if key not in keys:
        print(key)
        keys.append(key)
