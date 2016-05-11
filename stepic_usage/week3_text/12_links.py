import requests
import re

url_1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
url_2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'

urls = []
answer = 'No'

for x in range(2):
    urls.append(input().rstrip())

res = requests.get(urls[0])
first_step_text = res.text
all_inclusions = re.findall(pattern, res.text)
# print(all_inclusions)

for link in all_inclusions:
    temp_res = requests.get(link)
    links_in_str = re.findall(pattern, temp_res.text)
    # print(links_in_str)
    for link_2 in links_in_str:
        if link_2 == urls[1]:
            answer = 'Yes'
            break

print(answer)
'''
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:
Yes
'''