# 🚨 Don't change the code below 👇
row1 = ["🤣","🤣","🤣"]
row2 = ["🤣","🤣","🤣"]
row3 = ["🤣","🤣","🤣"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

vertical = int(position[0])
horizontal = int(position[1])

# first we need to access the position at the column level then we will specify its row position i=within that column
selected_column = map[horizontal - 1] 
selected_column[vertical - 1] = input("Please enter what u need to put there: ")

# or u can do this way.
# map[vertical - 1][horizontal - 1] = input("Please enter what u need to put there: ")
#

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
