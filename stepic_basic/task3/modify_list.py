def modify_list(l):
    i = 0
    e = 0
    lenght = len(l)
    while e < lenght:
        t = len(l)
        #print('len:', len(l))
        for x in l:
            #print('shag', i+e)
            #print('x:', x)
            if x == 0:
                l.remove(0)
                i += 1
            elif x % 2 != 0:
                l.remove(x)
                i += 1
            #print(i)
            #print(e)
        if t % 2 == 0:
            e += t // 2
        else:
            e += (t // 2) + 1
    #print(l)
    for y in l:
        l[l.index(y)] = y // 2

print(11 // 2)
lst = [10, 3, 1, 9, 11, 12, 31, 4, 0, 5, 70]
# [1, 3, 5, 7]
#[1, 2, 3, 4, 5, 6]
#[10, 3, 1, 9, 11, 12, 31, 4, 0, 5, 70]
print(lst)
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)

"""if x % 2 != 0:
    l.remove(x)
elif x % 2 == 0:
    l.append(x // 2)
    l.remove(x)
    #l.insert(x, (x // 2))"""


