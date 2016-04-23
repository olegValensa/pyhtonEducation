import sys

def join(lastKey):
    if 'url' in users and 'query' in users:
        for q in users['query']:
            for u in users['url']:
                print(lastKey + '\t' + q + '\t' + u)

lastKey = None
users = {}

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    category, name = value.strip().split(":")
    if lastKey and lastKey != key:
        join(lastKey)
        lastKey = key
        users.clear()
        users[category] = [name]
    elif lastKey and lastKey == key:
        if category in users:
            users[category].append(name)
        else:
            users[category] = [name]
    else:
        lastKey = key
        users[category] = [name]
if lastKey:
    join(lastKey)