import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_choice = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n "))
print(all_choice[user_choice])

computer_choice = random.randint(0,2)
print("Computer choose: ")
print(all_choice[computer_choice])


'''if user_choice == "0" and computer_choice == 1:
    print("You choose rock \n",all_choice[0])
    print("Computer choose paper \n",all_choice[1])
    print("Computer wins")
elif user_choice == "0" and computer_choice == 2:
    print("You choose rock \n",all_choice[0])
    print("Computer choose scissors \n",all_choice[2])
    print("You win")
elif user_choice == "0" and computer_choice == 0:
    print("You choose rock \n",all_choice[0])
    print("Computer choose rock \n",all_choice[0])
    print("Draw ")
elif user_choice == "1" and computer_choice == 0:
    print("You choose paper \n",all_choice[1])
    print("Computer choose rock \n",all_choice[0])
    print("You win")
elif user_choice == "1" and computer_choice == 2:
    print("You choose paper \n",all_choice[1])
    print("Computer choose scissors \n",all_choice[2])
    print("Computer wins")
elif user_choice == "1" and computer_choice == 1:
    print("You choose paper \n",all_choice[1])
    print("Computer choose paper \n",all_choice[1])
    print("Draw ")
elif user_choice == "2" and computer_choice == 0:
    print("You choose scissors \n",all_choice[2])
    print("Computer choose rock \n",all_choice[0])
    print("Computer wins")
elif user_choice == "2" and computer_choice == 1:
    print("You choose scissors \n",all_choice[2])
    print("Computer choose paper \n",all_choice[1])
    print("You win")
elif user_choice == "2" and computer_choice == 2:
    print("You choose scissors \n",all_choice[2])
    print("Computer choose scissors \n",all_choice[2])
    print("Draw")
else:
    print("Invalid choice")'''


