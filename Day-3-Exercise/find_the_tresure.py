print("Welcome to tresure Island.")
print("Your mission is to find the tresure.")
choice1 = input("which way do u wanna take Right or Left? ").lower()
choice2 = input("do u wanna Swim or Wait? ").lower()
choice3 = input("which door do u wanna get in? Red, Blue or Yellow?   ").lower()

if (choice1 == "left"):
  if (choice2 == "wait"):
    if (choice3 == "yellow"):
      print("Congratulation. You win!")
    else:
      print("Game over!")
  else:
    print("Game over!")
else:
  print("Game over!")
