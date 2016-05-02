s = input()
a = input()
b = input()

count = 0

if a in b and a in s:
    print('Impossible')
elif a == b:
    print(count)
else:
    while True:
        s = s.replace(a, b)
        count += 1
        if a not in s:
            break
    print(count)

print(s, a, b)
"""
aabbcc
aa
aaa
"""

