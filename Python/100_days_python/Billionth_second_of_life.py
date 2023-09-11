from datetime import datetime
age = int(input("What is your age?\n"))

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

