# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = name1 + name2
conv_to_lower = combined_names.lower()

t = conv_to_lower.count("t")
r = conv_to_lower.count("r")
u = conv_to_lower.count("u")
e = conv_to_lower.count("e")

true = t + r + u + e

l = conv_to_lower.count("l")
o = conv_to_lower.count("o")
v = conv_to_lower.count("v")
e = conv_to_lower.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}$, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your score is {love_score}$, you are alright together.")
else:
  print(f"Your score is {love_score}$.")
