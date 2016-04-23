'''
???????????? ?????? ?? ?? ???? ? ?????????????? ???? ????????.
? ?????? ?????? ???????? ????? ?????? ??? ????? ????? k ? l ????? ?????? � ?????????? ????????? ????, ????????????? ? ??????, ? ?????? ???????????? ?????????????? ??????,
??????????????. ? ????????? k ??????? ???????? ???? ???? ? ??????? "letter: code". ?? ???? ??? ?? ???????? ????????? ???????.
????? ????? ???? ??????????? ? ????? ???????. ? ???????? ???? ????? ??????????? ???? ???????? ????? ?????????? ????????;
?????? ?? ???? ???? ??????????? ? ?????? ???? ?? ???? ???. ???????, ? ????????? ?????? ???????? ?????????????? ??????.
???????? ?????? ? ???? ???? ???? ???????. ???????? ??? ?????, ??? ?????????????? ?????? ????? ??????????? ????????? ??????.

? ?????? ?????? ????????? ????? ???????? ?????? s. ??? ?????? ???????? ?? ???????? ???? ?????????? ????????.
?????????????, ??? ????? ??????????? ?????? ?? ??????????? 10^4 ????????.
'''
(k, l) = (int(x) for x in input().split())
#k = 4
#l = 14

max_len = 0
letter_dict = {}
for x in range(k):
    (letter, code) = (x for x in input().split(': '))
    letter_dict[code] = letter
    if len(code) > max_len:
        max_len = len(code)

#max_len = 3
#letter_dict = {'0': 'a','10': 'b','110': 'c','111':'d'}
#letter_dict = {'0': 'a'}

input_string = input()
#input_string = '0000'
#print(letter_dict)
#print(input_string)

start_char = 0
temp_len = max_len
output = ''
while start_char < l:
    len = start_char + temp_len
    tem_str = input_string[start_char:len]
    #print('temp letters', tem_str)
    if tem_str in letter_dict:
        #print('letter', letter_dict[tem_str])
        output += letter_dict[tem_str]
        start_char += temp_len
        temp_len = max_len
    else:
        temp_len -= 1
print(output)