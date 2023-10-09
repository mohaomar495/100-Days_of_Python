#Write your code below this line 👇

def prime_checker(number):
  primes = not_prime = 0
  for i in range(1, number+1):
    if number % i == 0:
      primes += 1
    else:
      not_prime += 1
  if primes == 2:
    print("Its a prime.")
  else:
    print("Its not a prime.")
      


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
