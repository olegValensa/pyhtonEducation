import csv

skills_user = {}
with open("files/Taleo_Experience_35.csv") as csvfile: #Taleo_Experience_35
    #for row in csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            number = row["Number"]
            skill = row["skills"]
            month = row["Month_Exper"]
        #number, skill, month = (x for x in reader)
            #print(number, skill, month)
            #key = str(number[1:-1] + ';' + month[1:-1])
            key = str(number + ':' + month)
            #print(key)
            if key not in skills_user:
                skills_user[key] = skill
            else:
                skills_user[key] =  skills_user[key] + str((',') + skill)

print (skills_user['13:200'])


with open('files/output.csv', 'w', newline='') as csvout:
    fields = ['Number,Months_Exp', 'Skills']
    writer = csv.DictWriter(csvout, fieldnames=fields, delimiter=':', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    #writer = csv.writer(csvout, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for key in skills_user:
        print(key)
        print(skills_user[key])
        writer.writerow({'Number,Months_Exp': key, 'Skills': '[' + skills_user[key] + ']'})

