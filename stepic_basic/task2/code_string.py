str_start = input()
str_new = ''
a = str_start[0]
c = 0
i = 0
for letter in str_start:
    i += 1
    if letter == a:
        c += 1
    else:
        str_new += (a + str(c))
        c = 1
    if i == len(str_start):
        str_new += (letter + str(c))
    a = letter
print(str_new)


