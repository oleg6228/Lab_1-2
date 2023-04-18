import re

with open('f.txt') as f:
    lines = f.readlines()

str = '*'
pattern = re.compile(re.escape(str))
with open('f.txt', 'w') as f:
    for line in lines:
        result = pattern.search(line)
        if result is None:
            f.write(line)

