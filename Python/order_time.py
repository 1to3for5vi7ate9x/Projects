import sys
"""order = int(input("What is the time? "))


min = order//60
sec = order % 60
if sec <= 9:
    print(str(min) + ":0" + str(sec))
else:
    print(str(min) + ":" + str(sec))

print(f"{min}:{sec//10}{sec%10}")

#time_in_min = format(time,".2f")

##################### Atm withdrawl ######################
amount = int(input("Enter the amount "))
if amount < 100 or amount > 10000 or amount % 100 !=0:
    sys.exit("Invalid amount ")

fivehnotes = amount//500
remaining_amount = amount%500
twohnotes = remaining_amount//200
remaining_amount_100 = remaining_amount%200
hundnotes = remaining_amount_100//100

print("500 x " + str(fivehnotes) + " = " + str(500*fivehnotes))
print("200 x " + str(twohnotes) + " = " + str(200*twohnotes))
print("100 x " + str(hundnotes)+ " = " + str(100*hundnotes))
#print(f"500 x {fivehnotes} = {fivehnotes*500}") -- For printing more properly

########################### Month and year

date = input("Enter date: ")
year,month,day = date.split("-") 
year,month,day = int(year),int(month),int(day)

#for year in range (1,3000):
    

#month = int(input("Enter the month number:")
if month > 12:
    sys.exit("Invalid month")

if month == 2 and year%4 == 0 and year%100 != 0 or year%400 == 0:
    print("Number of days is 29")
elif month == 2:
    print("Number of days is 28")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Number of days is 31")
else:
    print("Number of days 30")



#saved_month = (jan,feb,mar,april,may,june,july,aug,sep,oct,nov,dec)
#year = int(input("Enter the year: "))

    

######################## Split function

x = "hello"
y = "a-b"
z = "a-b-c"
q = x.split("-")
r,s = y.split("-")
v,t,u = z.split("-")

print(q,r,s,v,t,u)"""

#range(stop)
#range(start,stop)
#range(start,stop,step)
#x = range(5,14,3)
#y = list(x)
#print(y) -- Will give a list of x values as [5,14,3]
#for i in x: #can also be written as "for i in range(5,14,3)"
 #   print(i)

#n = int(input(": "))
"""for i in range(1,n+1):
    if i%3==0 and i%5!=0:
        print("sting")
    elif i%5==0 and i%3!=0:
        print("fanta")
    elif i%3*5==0:
        print("sprite")
    else:
        print(i)"""

# #improved above code
# for i in range(1,n+1):
#     if i%3==0 and i%5==0 :
#         print("sprite")
#     elif i%3==0:
#         print("sting")
#     elif i%5==0:
#         print("fanta")
    
#     else:
#         print(i)

# write program take input two numbers a and b.then find the even numbers between the first 2 no.

a = int(input("First: "))
b = int(input("Last: "))

# count = 0

# for i in range(a-1,b+2):
#     if i%2==0:
#         count += 1
# print(f"{count} even numbers between {a} and {b}")      

# input 2 numbers and find if they are an amiable pair. a,b are amicable pair, if sum of proper divisors of a equal to b and vice versa


divisors_of_a = []

 
