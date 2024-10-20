'''Prime and its Reverse
Description
Given an integer n, find out whether the number is prime and the reverse of the number is also a prime number.
If it is, then print "Yes" else "No".
Input Description
The first line of the input contains one integer t (1 ≤ t ≤ 10) - the number of test cases. Then t test cases follow.
The first line of each test case contains a single integer n (1 ≤ n ≤ 1000000000).'''

#Solution

import math
def Solve(num):
  # write your code here
  a = 0
  reverse = 0
  flag1 = 1
  flag2 = 1
  while num>0:
    a = num%10
    reverse = reverse*10+a
    num = num//10
  if n<=1 and reverse<=1:
    print("No")
  elif n == 2:
    print("Yes")
  elif n%2==0 or reverse%2==0:
    print("No")
    
  else:
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            flag1 = 0
            break
    for i in range(3,int(math.sqrt(reverse))+1,2):
        if reverse%i==0:
            flag2 = 0
    if flag1 and flag2:
        print("Yes")
  
    else:
        print("No")
      
t = int(input())

for _ in range(t):
    n = int(input())
    Solve(n)
