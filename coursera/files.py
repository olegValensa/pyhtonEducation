#7.1
count = 0
temp_variable = ()
sum_spam = 0.0
fh = open("../files/mbox-short.txt", "r")
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    temp_variable = line.strip().split()
    sum_spam += float(temp_variable[1])
    count += 1
fh.close()
print('Average spam confidence:', sum_spam/count)

#8.4
fh = open("../files/romeo.txt", "r")
lst = list()
for line in fh:
    words_in_line = line.rstrip().split()
    for word in words_in_line:
        if word in lst:
            continue
        else:
            lst.append(word)
fh.close()
lst.sort()
print(lst)

#8.5
fh = open("../files/mbox-short.txt", "r")
count = 0
for line in fh:
    if line.startswith("From ") :
        print(line.strip().split()[1])
        count += 1
fh.close()
print ("There were", count, "lines in the file with From as the first word")

#9.4
handle = open("../files/mbox-short.txt", "r")
sender = dict()
for line in handle:
    if line.startswith("From ") :
        sender_temp = (line.strip().split()[1])
        sender[sender_temp] = sender.get(sender_temp, 0) + 1
handle.close()
sended_max_mails = 0
result = ''
for mailer, count in sender.items():
    if count > sended_max_mails:
        sended_max_mails = count
        result = mailer + ' ' + str(count)
print(result)

#10.2
print()
print("task 10.2.............")
handle = open("../files/mbox-short.txt", "r")
hours = dict()
for line in handle:
    if line.startswith("From ") :
        hour_temp = (line.strip().split()[5]).split(':')[0]
        hours[hour_temp] = hours.get(hour_temp, 0) + 1
handle.close()
tmp = list((k,v) for (k,v) in hours.items())
tmp.sort()
for k,v in tmp:
    print(k, v)