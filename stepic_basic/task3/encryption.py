def create_dict(example, cipher):
    c = 0
    for l in example:
        dict_encr[l] = cipher[c]
        dict_decr[cipher[c]] = l
        c += 1

def encription(input):
    output = ''
    for l in input:
        output += dict_encr[l]
    return output

def decription(input):
    output = ''
    for l in input:
        output += dict_decr[l]
    return output


#word = 'abcd'
#cipher = '*d%#'
#encrypt = 'abacabadaba'
#decrypt = '#*%*d*%'

word = input()
cipher = input()
encrypt = input()
decrypt = input()

dict_encr = {}
dict_decr = {}
create_dict(word, cipher)
#print(dict_encr)
#print(dict_decr)
print(encription(encrypt))
print(decription(decrypt))