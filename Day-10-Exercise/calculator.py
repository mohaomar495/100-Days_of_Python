from replit import clear
from art import logo

print(logo)
def addition(n, m):
  return n + m


def subtraction(n, m):
  return n - m


def multiplication(n, m):
  return n * m


def division(n , m):
  if m != 0:
      return n / m
  return


operations = {
          "+": addition,
          "-": subtraction,
          "*": multiplication,
          "/": division
      }


def calculator():
  should_continue = True
  first_num = float(input("What's the first number?: "))
  for symbol in operations:
      print(symbol)
  while should_continue:
      operation = input("Pick an operation: ")
      second_num = float(input("What's the next number?: "))

      result = operations[operation](first_num, second_num)
      print(f"{first_num} {operation} {second_num} = {result}")

      another_try = input("Type 'y' to continue calculating with 10.0, or type 'n' to start a new calculations: ").lower()

      if another_try == "y":
          first_num = result
      else:
          should_continue = False
          clear()
          calculator()


def main():
  calculator()


if __name__ == "__main__":
  main()
