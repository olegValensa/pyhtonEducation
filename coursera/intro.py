try:
    _input = raw_input("Enter score between 0.0 and 1.0")
    score = float(_input)
    if score < 0.0:
        print('Out of range')
    elif score > 1.0:
        print('Out of range')
    elif score < 0.6:
        print('B')
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
except:
    print('Error')

# task 4.6
"""
def computepay(h,r):
    if h < 40:
        return h*r
    else:
        return 40*r + (h-40)*r*1.5
    return 42.37

hrs = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print (p)
"""

# task 5.2
largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break

        if largest is None:
            largest = int(num)
            smallest = int (num)

        if int(num) > largest:
            largest = int(num)
        elif int(num) < smallest:
            smallest = int(num)
        print (num)
    except:
        print ("Invalid input")

print ("Maximum", largest)
print ("Minimum", smallest)



