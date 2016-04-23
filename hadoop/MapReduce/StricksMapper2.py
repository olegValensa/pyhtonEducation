import sys

for line in sys.stdin:
    s = line.strip().split()

    for cat in s:
        dict = {}
        for letter in s:
            if letter != cat:
                if letter not in dict:
                    dict[letter] = 1
                else:
                    dict[letter] = dict[letter] + 1
        print(cat, end='\t')
        count = 0
        for d in dict:
            if count == 0:
                print(d + ':' + str(dict[d]),end='')
            else:
                print(',' + d + ':' + str(dict[d]),end='')
            count += 1
        print()