import requests
with open("files/dataset_3378_2 (1).txt") as f:
    s = f.readline().strip()
r = requests.get(s)
print(len(r.text.splitlines()))