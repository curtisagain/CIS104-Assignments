import calculator

num1 = float(input("Enter first number: "))
print("Select operation.")
print("+ Add")
print("- Subtract")
print("* Multiply")
print("/ Divide")
print("^ Power")
print("i Invert")
print("s Save")
print("r Recall")
print("c Clear Memory")
entry = input("> ")
num2 = float(input("Enter second number: "))



# all variables in main
while entry != 'X' and entry !='x':
  if entry == "+":
    calculator.add(num1,num2)

  elif entry == "-":
    calculator.subtract(num1,num2)

