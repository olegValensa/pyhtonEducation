import re
import sys

pattern = r"\b(a)+\b"

for line in sys.stdin:
    line = line.rstrip()
    new_line = re.sub(pattern, "argh", line, count=1, flags=re.IGNORECASE)
    print(new_line)
