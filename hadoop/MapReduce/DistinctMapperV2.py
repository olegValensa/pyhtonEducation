import sys

for line in sys.stdin:
    number, letter = line.strip().split(',')
    print(letter + '\t' + '1')