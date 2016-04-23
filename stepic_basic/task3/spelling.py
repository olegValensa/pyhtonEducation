def add_words(d):
    for w in range(d):
        w = input().lower()
        dict.append(w)

def str_input():
    l = int(input())
    for s in range(l):
        str = input().lower().split()
        for w in str:
            if w not in dict:
                dict.append(w)

dict = []
d = int(input())
add_words(d)
str_input()
for w in dict[d:]:
    print(w)