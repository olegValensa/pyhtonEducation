commands = []#'Insert 200', 'Insert 10', 'ExtractMax', 'Insert 500', 'Insert 20','ExtractMax']

n = int(input())
for x in range(n):
    commands.append(input())

chits = [0]
count = 0

for row in range(n):
    #print('------------LOOP------------')
    command = input().split()
    print('pr', command)
    if command[0] == 'Insert':
        if chits[count] < int(command[1]):
            chits[count] = int(command[1])
    elif command[0] == 'ExtractMax':
        print(chits[count])
        chits.append(0)
        count += 1
