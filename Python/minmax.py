def minmax():
    num = []
    n = int(input("Enter the number of element "))
    for i in range(n):
        numbers = int(input(f"Enter number {i+1}: "))
        num.append(numbers)
    min = num[0]
    for i in num:
        if min>i:
            min = i
    print(min)


minmax()
