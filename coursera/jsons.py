#14 json in Python 2.7 syntax
import urllib as U
import json
'''
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_184253.json'
print ('Retrieving', url)
uh = U.urlopen(url)
data = uh.read()
js = json.loads(str(data))
comments_sum = 0
print ('Count:', len(str(data)))
print ('Count:', len(js["comments"]))
for comment in js["comments"]:
    comments_sum += int(comment["count"])
print ('Sum:', comments_sum)
'''
event = "{\"key3\": \"value3\",\"key2\": \"value2\"}"
js_event = json.dumps(str(event))
print(js_event['key2'])

