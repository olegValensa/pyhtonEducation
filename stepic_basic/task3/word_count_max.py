def word_count(lst):
    for w in lst:
        if w not in dictionary:
            dictionary[w] = 1
        else:
            dictionary[w] = dictionary[w] + 1

def most_word(dict):
    popular_word = ''
    value = 0
    for w in dict:
        if dict[w] > value:
            value = dict[w]
            popular_word = w
        elif dict[w] == value and w < popular_word:
            popular_word = w
    print(popular_word, value)

dictionary = {}
with open("files/dataset_3363_3.txt") as f:
    for line in f:
        word_count(line.strip().lower().split())

most_word(dictionary)
