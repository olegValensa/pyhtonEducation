import requests
with open("files/dataset_3378_3.txt") as f:
    s = f.readline().strip()
dir = 'https://stepic.org/media/attachments/course67/3.6.3/'
r = requests.get(s)
txt = ''
while txt[:2] != 'We':
    r = requests.get(dir + r.text.strip())
    txt = r.text.strip()
    print(txt)

