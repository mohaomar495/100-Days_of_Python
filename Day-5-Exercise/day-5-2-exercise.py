#Author: Mohammad Adde 

scores = input("please enter scores: ").split()
highest_score = 0
for score in scores:
  score = int(score)
if score > highest_score:
  highest_score = score
  print(f"highest score is: {highest_score}")
