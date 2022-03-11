from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def calculator():
  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
  }

  num1 = float(input("What's the first number?: "))

  condition = True
  while condition == True:
    for symbol in operations:
      print(symbol, end = ' ')
    operation_symbol = input("\nPick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to calculate a new number.: ")
    if cont == 'y':
      num1 = answer
    else:
      print("Thank you for using the pythonista calculator.")
      condition = False
      calculator()

calculator()