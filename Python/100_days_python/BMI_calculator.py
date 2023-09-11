print("Welcome to BMI calculator ")
height = float(input("Enter your height in m: "))
weight = int(input("Enter yout weight in kg: "))

bmi = weight/height **2
final_bmi = round(bmi,2)
if final_bmi < 18.5:
    print("You are under weight. ")
elif final_bmi >= 18.5:
    print("You are in normal weight. ")
elif final_bmi >= 25.0:
    print("You are in overweight. ")
elif final_bmi >= 30.0:
    print("You are obese. ")
else:
    print("You are clinically obese. ")
print(f"Your BMI is {final_bmi}")



