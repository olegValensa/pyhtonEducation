import requests
import re

# res = requests.get('https://wiki.ciklum.net/download/attachments/115819227/List2_31k.csv')

# print(res.content)

pattern_url = r'<a\s+(?:[^>]*?\s+)?href="([^"|^\']*)"'
pattern_domain = r'(?:https?:\/\/)?(?:www\.)?(.*?)\/'

with open('files/test_url.txt', 'r') as f:
    for line in f:
        new_line = line.replace('\'', '\"').rstrip()
        url = re.findall(pattern_url, new_line)
        print(new_line)
        print(url)
        print()



