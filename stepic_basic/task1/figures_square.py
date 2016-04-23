figure = input()
if figure == '???????????':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = p*(p-a)*(p-b)*(p-c)
    print(S**0.5)
elif figure == '?????????????':
    a = int(input())
    b = int(input())
    print(float(a*b))
elif figure == '????':
    r = int(input())
    print(float(3.14 * r * r))
