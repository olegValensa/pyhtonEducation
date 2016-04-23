from pymongo import MongoClient
import datetime
import csv

countFiles = 0

#my_date_str = "2016-03-03T11:35:00Z"
#my_date_end = "2016-03-03T12:00:00Z"

my_datetime_start = datetime.datetime(2016, 3, 3, 11, 35, 0)
my_datetime_end = datetime.datetime(2016, 3, 3, 12, 0, 0)

client = MongoClient('biowave.pp.ciklum.com', 27017)
db = client.test
collection = db.data
docs = (collection.find({ "topic": "nodes/accel_sky/accelx", '$and': [ { "date": { '$gt': my_datetime_start } },{ '$and': [ { "date": { '$lt': my_datetime_end } } ] } ] }))
for doc in docs:
    print(doc['date'], doc['payload']['buf'])

print(docs)


