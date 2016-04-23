import csv

countFiles = 0
with open("D:/Inabi/ToFC40000leads6.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    filepath = 'leads' + str(countFiles) + '.csv'
    for row in reader:

        id = row["Account ID"]
        firstname = row["First Name"]
        lastname = row["Last Name"]
        country = row["Country Name"]
        email = row["Email"]
        phone = row["Phone"]
        user = row["File Loader"]
        depositAmount = row["Deposit Amount"]

        with open(filepath, 'ab') as writefile:
            wr = csv.writer(writefile, quoting=csv.QUOTE_ALL)
            wr.writerow([id, firstname, lastname, country, email, phone, user, depositAmount])

        if (int(id) % 300) == 0:
            countFiles += 1
            filepath = 'leads' + str(countFiles) + '.csv'
            with open(filepath, 'ab') as writefile:
                wr = csv.writer(writefile, quoting=csv.QUOTE_MINIMAL)
                wr.writerow(["Account ID","First Name","Last Name","Country Name","Email","Phone","File Loader","Deposit Amount"])

