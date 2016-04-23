n = int(input())
dir_east = 0
dir_north = 0
for a in range(n):
    str = input().split()
    if str[0] == 'east':
        dir_east += int(str[1])
    elif str[0] == 'west':
        dir_east -= int(str[1])
    elif str[0] == 'north':
        dir_north += int(str[1])
    elif str[0] == 'south':
        dir_north -= int(str[1])
print(dir_east, dir_north)
