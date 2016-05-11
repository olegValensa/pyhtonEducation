import re
import sys

pattern = r"(\w)\1{1,}"

for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(pattern, r"\1", line)
    print(new_line)
