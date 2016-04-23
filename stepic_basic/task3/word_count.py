def word_count(str):
    d = {}
    for s in str:
        if s not in d:
            d[s] = 1
        else:
            d[s] = d[s] + 1

    for t in d:
        print(t, end=' ')
        print(d[t])



str = input().lower().split()
word_count(str)
