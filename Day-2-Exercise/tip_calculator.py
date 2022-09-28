#this is a project that calculates you the tip.

print("welcome to the tip calculator.")
total_bill = float(input("what was the total bill? "))
percentage_tip = float(input("what percentage would like to give? 10, 12, or 15? "))
numb_of_people = int(input("How many people to split the bill? "))
total = (total_bill / numb_of_people) * ((percentage_tip + 100) / 100)

print(f"each person should pay {round(total, 2)}")
