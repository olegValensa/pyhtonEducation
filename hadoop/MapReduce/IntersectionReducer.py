import sys

temp = {}
temp_str = ''
for line in sys.stdin:
    element, bunch = line.strip().split('\t')
    if element not in temp:
        temp[element] = set(bunch)
    else:
        temp[element].add(bunch)
    if element == temp_str and len(temp[element]) > 1:
        print(element)
        temp.clear()
    temp_str = element
