def parse_match(match):
    lst = []
    elements = match.split(';')

    if elements[0] not in talbe:
        if elements[1] > elements[3]:
            talbe[elements[0]] = [1, 1, 0, 0, 3]
        elif elements[1] == elements[3]:
            talbe[elements[0]] = [1, 0, 1, 0, 1]
        else:
            talbe[elements[0]] = [1, 0, 0, 1, 0]
    else:
        if elements[1] > elements[3]:
            lst = talbe[elements[0]]
            lst[0] += 1
            lst[1] += 1
            lst[4] += 3
            talbe[elements[0]] = lst
        elif elements[1] == elements[3]:
            lst = talbe[elements[0]]
            lst[0] += 1
            lst[2] += 1
            lst[4] += 1
            talbe[elements[0]] = lst
        else:
            lst = talbe[elements[0]]
            lst[0] += 1
            lst[3] += 1
            talbe[elements[0]] = lst

    if elements[2] not in talbe:
        if elements[1] < elements[3]:
            talbe[elements[2]] = [1, 1, 0, 0, 3]
        elif elements[1] == elements[3]:
            talbe[elements[2]] = [1, 0, 1, 0, 1]
        else:
            talbe[elements[2]] = [1, 0, 0, 1, 0]
    else:
        if elements[1] < elements[3]:
            lst = talbe[elements[2]]
            lst[0] += 1
            lst[1] += 1
            lst[4] += 3
            talbe[elements[2]] = lst
        elif elements[1] == elements[3]:
            lst = talbe[elements[2]]
            lst[0] += 1
            lst[2] += 1
            lst[4] += 1
            talbe[elements[2]] = lst
        else:
            lst = talbe[elements[2]]
            lst[0] += 1
            lst[3] += 1
            talbe[elements[2]] = lst


talbe = {}
n = int(input())
for m in range(n):
    m = input()
    parse_match(m)

for team in talbe:
    print(team, end=':')
    for p in talbe[team]:
        print(str(p), end=' ')
    print()