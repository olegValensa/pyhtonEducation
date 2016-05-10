import re
import sys

pattern = r"human"

for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(pattern, "computer", line)
    print(new_line)
