student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
sum = 0
total_heights=0
for i in student_heights:
    sum = sum + i
    total_heights += 1

avg_height = sum/total_heights
round_avg_height = round(avg_height)
print(round_avg_height)


