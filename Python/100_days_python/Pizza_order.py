print("Welcome to Pizza Deliveries")
size = input("What size of pizza you want? S,M and L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
    else:
        pass
elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
    else:
        pass
elif size == 'L':
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3
    else:
        pass
else:
    print("Invalid input")
if extra_cheese == 'Y':
    bill +=1
    print(f"Your total bill is {bill}$")
else:
    print(f"Your total bill is {bill}$")
