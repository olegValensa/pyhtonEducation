import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

# [] -- можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]

pattern = r"\bcat\b"
string = "catapult and cat"
match_object = re.match(pattern, string)
print(match_object)

string = "catapult and cat"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

string = "catapult and cat"
is_inclusions = re.search(pattern, string)
print(is_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

pattern = r"((\w+)-\2)"
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates)
