from pymongo import MongoClient
import csv

countFiles = 0

client = MongoClient('172.28.27.148', 27017)
db = client.mongodb
collection = db.enrichedLead
emails = set(collection.distinct("email"))
#print(emails)

filepath = 'leads36.csv'


with open("D:/Inabi/1000/11/leads6.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = row["Account ID"]
        firstname = row["First Name"]
        lastname = row["Last Name"]
        country = row["Country Name"]
        email = row["Email"]
        phone = row["Phone"]
        user = row["File Loader"]
        depositAmount = row["Deposit Amount"]

        if email not in emails:
            print(row)
            with open(filepath, 'ab') as writefile:
                wr = csv.writer(writefile, quoting=csv.QUOTE_MINIMAL)
                wr.writerow([id, firstname, lastname, country, email, phone, user, depositAmount])