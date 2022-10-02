# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

seed_code = random.seed(input("Please enter the seed code: "))

length_of_names = len(names)

random_name = random.randint(0, (length_of_names - 1))

the_person_paying = names[random_name]

print(f"{the_person_paying} is paying the bill")
