import urllib
from BeautifulSoup import *

#12.1
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_184252.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

comments_sum = 0
tags = soup('span')
for tag in tags:
    comments_sum += int(tag.contents[0])
print ('Sum:', comments_sum)


#12.2
count = 7
position = 18
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Lilias.html'

i = 0
while (i<count):
    url_step = url
    html = urllib.urlopen(url_step).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position-1].get('href', None)
    i += 1
print(tags[position-1].contents[0])
