import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split()
# total_persons = len(names)
# #print(a)
# i = random.randint(0,total_persons-1)
# person_who_will_pay = names[i]

person_who_will_pay = random.choice(names)
print( person_who_will_pay +" is going to buy the meal today! ")