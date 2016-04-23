import sys

filterWord = 'user10'

for line in sys.stdin:
    s = line.strip().split('\t')[1]
    if s == filterWord:
        print(line.strip())

for line in sys.stdin:
    print(line.strip().split('\t')[2])
