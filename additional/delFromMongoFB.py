from pymongo import MongoClient
import csv

countFiles = 0

client = MongoClient('172.28.27.148', 27017)
db = client.mongodb
collection = db.enrichedLead

emails = (collection.find({"timestamp":1456000000000}))
#collection.update({"email":"afruj@hotmail.com"},{'facebookInfoByEmail':1}, False, True);


for document in emails:
    #print(document)
    if 'facebookInfoByEmail' in document:
        if len(document['facebookInfoByEmail']) == 2 and "fullContactByEmail" in document:
            print(document['email'])
            print(len(document))


'''
for document in emails:
    #print(document)
    if document['email'] == 'afruj@hotmail.com':
        print(document)
        collection.update({"email":"afruj@hotmail.com"},{'facebookInfoByEmail':1}, False, True);
        '''
#collection.delete_one({"email":document["email"]})