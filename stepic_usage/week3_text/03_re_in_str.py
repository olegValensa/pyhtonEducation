import re
import sys

pattern = r"cat"

for line in sys.stdin:
    line = line.rstrip()
    all_inclusions = re.findall(pattern, line)
    if len(all_inclusions) > 1:
        print(line)
