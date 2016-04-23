# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json
import csv

client = MongoClient('172.28.27.148', 27017)

db = client.mongodb

'''collection = db.enrichedLead

cursor = collection.find({ "fullContactByEmail.socialProfiles.typeId": "facebook", "facebookInfoByEmail": None })

for document in cursor:
    print(document["email"])'''

dictionary = {}

with open("D:/Inabi/ToFC1000leads2.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        email = row["Email"]
        depositAmount = row["DepositAmount"]
        dictionary[email] = depositAmount

#print(dictionary)

collection = db.rawLeads
cursor = collection.find({"fileLoader":"1", "depositAmount": None})
for document in cursor:
    #if document["email"] == 'canko.kolovsky@gmail.com':
    #   collection.update({'email' : document["email"]}, {'$set' : {'depositAmount' : '2000' }})
    leadId = document["email"]
    if leadId in dictionary:
        print(leadId, dictionary[leadId])
        collection.update({'email' : leadId}, {'$set' : {'depositAmount' : dictionary[leadId] }})
    #print(document["accountId"],document["email"],dictionary[document["email"]])