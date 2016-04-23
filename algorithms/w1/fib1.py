
a = 23#47905881698199969
b = 6#76940
print(a % b)


'''
#1
n = int(input())
i = 2
fib_array = [1]*(n+1)
fib_array[0] = 0
for d in fib_array[2:]:
    fib_array[i] = fib_array[i-1] + fib_array[i-2]
    i += 1
print(fib_array[n])

#2
n = int(input())
i = 2
fib_array = [1]*(n+1)
fib_array[0] = 0
for d in fib_array[2:]:
    fib_array[i] = (fib_array[i-1] % 10 + fib_array[i-2] % 10) % 10
    i += 1
print(fib_array[n])
'''

#3
#n, m = input().split()
n, m = (int(x) for x in input().split())
i = 2
num_prev = 1
num_prev_prev = 0
value = 0
period = 0

while i < n:
    value = (num_prev + num_prev_prev) % m
    if (value == 1) and (num_prev == 0):
        period = i - 1
        i = 2
        break
    num_prev_prev = num_prev
    num_prev = value
    i += 1

period_array = [0]*period
period_array[1] = 1
for v in period_array[2:]:
    period_array[i] = (period_array[i-1] + period_array[i-2]) % m
    i += 1

print(period_array[n % period])
