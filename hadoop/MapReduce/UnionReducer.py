import sys

temp = ''
for line in sys.stdin:
    element, bunch = line.strip().split('\t')
    if element != temp:
        print(element)
    temp = element
