print("Welcome to the treasure island. ")
print("Your mission is to find the treasure. ")
road = input("You\'re at the cross road. Where you want to go type 'left' or 'right' ").lower()
if road == 'left':
    lake = input("You came to a lake. There is the island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if lake == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour you choose? \n").lower()
        if door == 'red':
            print("You opened the door to a room full of lions 🦁. Game Over 💀")
        elif door == 'yellow':
            print("You\'ve have found treasure 🏆. You win!!! \n")
        else:
            print("You entered the room with a monster 👹. Game Over 💀")
    else:
        print("You were caught by an crocodile 🐊. Game Over 💀")

else:
    print("You died because right is not always right. Game Over 💀")

