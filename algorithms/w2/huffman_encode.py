'''
??????????? ????????
?? ?????? ???????? ?????? s ????? ?? ????? 104, ????????? ?? ???????? ???? ?????????? ????????, ????????? ??????????? ????????????? ???.
? ?????? ?????? ???????? ?????????? ????????? ???? k, ????????????? ? ??????, ? ?????? ???????????? ?????????????? ??????.
? ????????? k ??????? ???????? ???? ???? ? ??????? "letter: code". ? ????????? ?????? ???????? ?????????????? ??????.
'''

# making tree function
def make_leaf(symbol, weight):
    return (symbol, weight)

def is_leaf(x):
    return isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], int)

def get_leaf_symbol(leaf):
    return leaf[0]

def get_leaf_weight(leaf):
    return leaf[1]

def get_left_branch(huff_tree):
    return huff_tree[0]

def get_right_branch(huff_tree):
    return huff_tree[1]

def get_symbols(huff_tree):
    if is_leaf(huff_tree):
        return [get_leaf_symbol(huff_tree)]
    else:
        return huff_tree[2]

def get_freq(huff_tree):
    if is_leaf(huff_tree):
        return get_leaf_weight(huff_tree)
    else:
        return huff_tree[3]

def make_tree(left_branch, right_branch):
    return [left_branch, right_branch, get_symbols(left_branch) + get_symbols(right_branch), get_freq(left_branch) + get_freq(right_branch)]

def encode(symbols, tree):
    encoding = []
    for s in symbols:
        encoding.extend(encode_symbol(s,tree))
    return encoding

def encode_symbol(s, tree):
    encoding = []
    curr_branch = tree
    while not is_leaf(curr_branch):
        if not s in get_symbols(curr_branch):
            return 'ERROR: Symbol not in tree'
        elif s in get_symbols(get_left_branch(curr_branch)):
            encoding.append(0)
            curr_branch = get_left_branch(curr_branch)
        elif s in get_symbols(get_right_branch(curr_branch)):
            encoding.append(1)
            curr_branch = get_right_branch(curr_branch)
        else:
            return 'ERROR: Symbol in neither branch'
    return encoding

#overall functions
def create_dictionary(input_string):
    for l in input_string:
        if l not in dict_freq:
            dict_freq[l] = 1
        else:
            dict_freq[l] = dict_freq[l] + 1

# first tree
#ht01 = make_tree(make_leaf('A',4), make_tree(make_leaf('B', 2), make_tree(make_leaf('C', 1), make_leaf('D', 1))))
input_string = 'abacabad'
dict_freq = {}
create_dictionary(input_string)
list_values = list(dict_freq.items())
list_values.sort(key=lambda item: item[1])

while len(list_values) != 1:
    temp_banch = make_tree(list_values[0],list_values[1])
    list_values.append(temp_banch)
    del list_values[0]
    del list_values[0]
    list_values.sort(key=lambda item: get_freq(item))
tree = list_values[0]
print(tree)
output = ''
dict_code = {}
for letter in input_string:
    letter_code = ''
    letter_array = encode_symbol(letter, tree)
    for x in letter_array:
        letter_code += str(x)
    if letter not in dict_code:
        dict_code[letter] = letter_code
    output += letter_code
if len(dict_freq) == 1:
    dict_code[input_string[0]] = '0'
    for letter in input_string:
        output += '0'
print(len(dict_freq), len(output))
for l in sorted(dict_code):
    print(l + ':', dict_code[l])
print(output)