def main():
    n = int(input("Enter a number: "))
    print(prime_checker(number=n))
    
def prime_checker(number):
    if number == 1: return False
    for i in range(2, number):
        if number % i == 0:
            return "It's a prime number."
    return "It's not a prime number."

#TEST
#for n in range(1, 100):
        #print(n, prime_checker(n))
        
main()