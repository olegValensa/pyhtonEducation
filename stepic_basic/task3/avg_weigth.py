d = {}
for a in range(1, 12):
    d[a] = [0,0]

with open("files/dataset_3380_5 (2).txt") as f:
    for line in f:
        tap = line.strip().split('\t')
        temp_lst = d[int(tap[0])]
        temp_lst[0] += int(tap[2])
        temp_lst[1] += 1
        d[int(tap[0])] = temp_lst

with open("files/output.txt", "w") as f:
    for c in d:
        f.write(str(c))
        f.write(' ')
        temp_lst = d[c]
        #print(temp_lst)
        if temp_lst[1] == 0:
            f.write('-')
        else:
            a = temp_lst[0]/temp_lst[1]
            f.write(str(a))
        f.write('\n')
