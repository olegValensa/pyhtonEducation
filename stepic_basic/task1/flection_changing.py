n = 252
centuria = n % 100
dexia = centuria // 10
unaria = centuria % 10
if (unaria == 1 and dexia != 1): print(n, 'programist')
elif (unaria == 0): print(n, 'programistov')
elif (5 <= unaria <= 9): print(n, 'programistov')
elif (10 <= centuria <= 14): print(n, 'programistov')
else: print(n, 'programista')

#if a % 100 == 1

print(n , centuria , dexia, unaria)