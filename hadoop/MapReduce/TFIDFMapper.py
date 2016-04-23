import sys
import re

for line in sys.stdin:
    doc, text = line.strip().split(':', 1)
    for word in (re.findall(r"[\w']+", text)):
        print(word + '#' + doc + '\t1')
