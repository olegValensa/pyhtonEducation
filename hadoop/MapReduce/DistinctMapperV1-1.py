import sys

for line in sys.stdin:
    key, value = line.strip().split('\t')
    categories = value.split(',')
    for cat in categories:
        print(key + ',' + cat + '\t' + '1')