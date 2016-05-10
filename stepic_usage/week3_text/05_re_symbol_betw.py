import re
import sys

pattern = r"z...z"

for line in sys.stdin:
    line = line.rstrip()
    match_object = re.search(pattern, line)
    if match_object:
        print(line)
