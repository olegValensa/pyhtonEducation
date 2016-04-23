f = open("files/dataset_3363_2.txt", "r")
s = f.readline()
f.close()
#s = 'a3b4c2e10b1'
str = ''
str_digit = ''
str_letter = s[0]
for i in s[1:]:
    if i.isalpha():
       str = str + (str_letter * int(str_digit))
       str_letter = i
       str_digit = ''
    elif i.isdigit():
        str_digit = str_digit + i
str = str + (str_letter * int(str_digit))

with open('files/out.txt', 'w') as ouf:
    ouf.write(str)
print(str)