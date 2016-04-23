a = 180.0234
print("%8.3f" % a)


days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

x , y = 3, 4
print(y)

stuff = dict()
print (stuff.get('candy',-1))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print (friends[0])

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)

x = '40'
y = int(x) + 2
print (y)

x = 'From marquard@uct.ac.za'
print (x[8])

x = 'From marquard@uct.ac.za'
print (x[14:17])

print (len('banana')*7)

greet = 'Hello Bob'
print (greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print (data[pos:pos+3])


text = "X-DSPAM-Confidence:    0.8475";
num = text.find('0')
fl = float(text[num:])
print(fl)

ar = input().split()
sum = 0
for i in ar:
    sum += int(i)
print(sum)