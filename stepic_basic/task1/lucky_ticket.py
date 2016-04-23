t = int(input())
first = t // 1000
f_3 = first % 10
f_2 = (first // 10) % 10
f_1 = first // 100
second = t % 1000
s_3 = second % 10
s_2 = (second // 10) % 10
s_1 = second // 100
print(first, second)
print(f_1, f_2, f_3)
print(s_1, s_2, s_3)
if (f_1 + f_2 + f_3)==(s_1 + s_2 + s_3): print('Lucky')
else: print('Common')
