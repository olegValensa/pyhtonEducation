#13 xml
import xml.etree.ElementTree as ET
#changes due to python3: added .request
import urllib.request as U

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_184249.xml'
print('Retrieving', url)
uh = U.urlopen(url)
tree = ET.fromstring(uh.read())
lst = tree.findall('comments/comment')
print('Count:', len(lst))
comments_sum = 0
for i in lst:
    comments_sum += int(i.find('count').text)
print('Sum:', comments_sum)



#12
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
#changes due to python3: added .encode()
mysock.send("GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n".encode())

while True:
    #changes due to python3: added .decode()
    data = mysock.recv(512).decode()
    if ( len(data) < 1 ) :
        break
    print (data)

mysock.close()



import re

sum = 0
with open("files/regex_sum_184247.txt") as f:
    for line in f:
        y = re.findall('[0-9]+', line)
        if len(y) > 0:
            print(y)
            for element in y:
                sum += int(element)
print(sum)
