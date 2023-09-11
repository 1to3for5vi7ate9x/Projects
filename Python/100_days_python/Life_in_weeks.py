# Based on the article by Tim Urban at waitbutwhy.com -->your life in weeks
age = int(input("What is your current age? \n"))

years_left = 90 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
age_till_billion = 31 - age
#print(age_till_billion)
t = 365*24*60*60
seconds_till_bill = (age_till_billion*t)
#print(t)
#print(t+seconds_till_bill)
print(f"You have {seconds_till_bill}seconds left to reach 1 Billion second of your life ")
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left.")

