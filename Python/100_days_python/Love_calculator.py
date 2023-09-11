import random

print("Welcome to Love calculator: ")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

lower_name1 = name1.lower()
lower_name2 = name2.lower()


count_true_love1 = lower_name1.count("t")+ lower_name1.count("r")+ lower_name1.count("u")+lower_name1.count("e")+lower_name1.count("l")+lower_name1.count("o")+lower_name1.count("v")
count_true_love2 = lower_name2.count("t")+ lower_name2.count("r")+ lower_name2.count("u")+lower_name2.count("e")+lower_name2.count("l")+lower_name2.count("o")+lower_name2.count("v")

#score = str(count_true_love1)+str(count_true_love2)
score = random.randint(1,100)
int_score = int(score)
if (int_score < 10) or (int_score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (int_score > 40) or (int_score < 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")


#print(love)
#print(true)
