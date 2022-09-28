# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)
# days in year = 365 days
# weeks in year = 52 weeks
# months in year = 12 months

#years left
years_left = 90 - age

#Days left
days_left = years_left * 365

#weeks left
weeks_left = years_left * 52

#months left
months_left = years_left * 12

#print the days, weeks and months left.
print(f"you have {days_left} days, {weeks_left} weeks, {months_left} months left")
