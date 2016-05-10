import re
import sys

pattern = r"(\b\w\w)"
str = "this is a text"
a = re.findall(pattern, str)
print(a)
b = re.sub(pattern, r"\2\1", str)
print(b)

'''
for line in sys.stdin:
    line = line.rstrip()s
    new_line = re.sub(pattern, "argh", line, count=1, flags=re.IGNORECASE)
    print(new_line)
'''