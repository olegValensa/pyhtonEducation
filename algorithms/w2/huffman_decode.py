# making tree function
def make_leaf(symbol, weight):
    return (symbol, weight)

def is_leaf(x):
    return isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], float)

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

def select_branch(bit, tree):
    if bit == '0':
        return get_left_branch(tree)
    elif bit == '1':
        return get_right_branch(tree)
    else:
        return 'ERROR: Incorrect bit'

def decode(bits, tree):
    if bits == []:
        return []
    curr_branch = tree
    next_branch = None
    decoding = []
    while bits != []:
        next_branch = select_branch(bits[0], curr_branch)
        if is_leaf(next_branch):
            decoding.append(get_leaf_symbol(next_branch))
            curr_branch = tree
        else:
            curr_branch = next_branch
        del bits[0]
    return decoding

#overall functions
(k, l) = (int(x) for x in input().split())
#k = 4
#l = 14
letter_code = []
for x in range(k):
    (letter, code) = (x for x in input().split(': '))
    letter_code.append((letter, code))
#letter_code = [('a', '0'),('b', '10'),('c', '111'),('d', '110')]

input_string = input()
#input_string = '01001100100111'
input_array = []
for x in input_string:
    input_array.append(x)
#print(input_string)
#print(input_array)

i = 0
for (letter, code) in letter_code[:k]:
    letter_code.append((letter, 1/len(code)))
    del(letter_code[0])

letter_code.sort(key=lambda item: item[1])
#print(letter_code)
if k > 0:
    while len(letter_code) != 1:
        temp_banch = make_tree(letter_code[0],letter_code[1])
        letter_code.append(temp_banch)
        del letter_code[0]
        del letter_code[0]
        letter_code.sort(key=lambda item: get_freq(item))

    tree = letter_code[0]
#print(tree)

    decoded = decode(input_array, tree)
if k == 1:
    print(letter_code[0][0]*len(input_string))
elif k == 0:
    print()
else:
    for letter in decoded:
        print(letter,end='')