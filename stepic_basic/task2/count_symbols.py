str = input()
c = s = 0
for letter in str.lower():
    if (letter == 'c' or letter == 'g'):
        c += 1
    s += 1
print((c / s) * 100)
