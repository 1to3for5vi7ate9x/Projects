print("Welcome to the tip calculator .")
amount = float(input("What is your total bill? $"))
members = int(input("How many people to split the bill ? "))
tip = int(input("What percentage tip wpuld you like to give ? 10, 12, or 15? "))
bill = 0
if tip == 10:
    bill = (amount/members)*0.10 + (amount/members)
elif tip == 12:
    bill = (amount/members)*0.12 + (amount/members)
else:
    bill = (amount/members)*0.15 + (amount/members)
final_bill = "{:.2f}".format(bill)
print(f"Each person should pay: ${final_bill}")



