# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json

addTimestamp = 1456000000000

client = MongoClient('172.28.27.148', 27017)

#'''
db = client.mongodb
collection = db.enrichedLead
print(db.collection_names(include_system_collections=False))

#'''
emails = (collection.distinct("email"))
print (len(emails))

f = open('D:/Inabi/1000/enrichedLead3/part-00001_new', 'r')
lines = f.readlines()
lines = map(lambda x: json.loads(x.rstrip()), lines)
f.close()
print(len(lines))
'''

'''
count = 0
for line in lines:
    if 'email' in line.keys():
        if len(line["email"]) > 1:
            if line["email"] in emails:
                pass
            else:
                emails.add(line["email"])
                line["timestamp"] = addTimestamp
                print(line)
                del line["_id"]
                collection.insert(line)
                count += 1
print(count)
#'''