row1 = ["🟨","🟨","🟨"]
row2 = ["🟨","🟨","🟨"]
row3 = ["🟨","🟨","🟨"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where you want to put treasure? "))

column = position//10
row = position % 10

selected_row = map[row-1]
selected_row[column-1]="❌"

print(f"{row1}\n{row2}\n{row3}")

#print(map)
#print(column,row)



