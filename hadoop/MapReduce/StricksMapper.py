import sys

for line in sys.stdin:
    s = line.strip().split()
    for cat in s:
        for letter in s:
            if letter != cat:
                print(cat + ',' + letter + '\t' + '1')