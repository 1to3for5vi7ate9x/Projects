a = int(input("First: "))
b = int(input("Second: "))

x = 0
for i in range(1,a):
    if a % i ==0:
        x += i

y=0
for i in range(1,b):
    if b % i == 0:
        y += i
        
if x==b and y==a:
    print("Amicable pair")
else:
    print("Not Amicable pair")