import json

f = open('files/part-0000', 'r')
lines = f.readlines()
lines = map(lambda x: json.loads(x.rstrip()), lines)
f.close()

filepath = 'files/part-00001'

keys = set()

#with open(filepath, 'ab') as writefile:

for line in lines:
    if 'email' in line.keys():
        if line["email"] not in keys:
            keys.add(line["email"])
            with open(filepath, 'a') as writefile:
                json.dump(line, writefile)
                writefile.write('\n')
            print(line)
    elif 'phone' in line.keys():
        if line["phone"] not in keys:
            keys.add(line["phone"])
            with open(filepath, 'a') as writefile:
                json.dump(line, writefile)
                writefile.write('\n')
            print(line)

print(keys)

