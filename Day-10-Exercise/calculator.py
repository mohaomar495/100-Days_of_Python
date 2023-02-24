from replit import clear
from art import logo
print(logo)

def add (i, j):
  """Returns the addition of two given inputs"""
  return i + j
def subtract(i , j):
  """Returns the subtraction of two given inputs"""
  return i - j
def mult(i , j):
  """Returns the multiplication of two given inputs"""
  return i * j
def div(i , j):
  """Returns the division of two given inputs"""
  return i / j

operations = {
  "+":add,
  "-":subtract,
  "*":mult,
  "/":div
}

def calculator():
  """Here is calculator which can calculate most of the math basics using +/-/*/'/(division)'."""
  i = float(input("Enter the first number: "))

  for sympol in operations:
    print(sympol)

  should_continue = True

  while should_continue:
    choice = input("Pick an operation: ")
    j = float(input("Enter the next number: "))
    calculation = operations[choice]
    result = calculation(i, j)

    print(f"{i} {choice} {j} = {result}")

    To_continue = input("Type 'y' to continue calculating with the current {result}, or type 'n' to start a new calculation: ").lower()
    if To_continue == "y":
      i = result
    else:
      should_continue = False
      clear()
      calculator()
calculator()