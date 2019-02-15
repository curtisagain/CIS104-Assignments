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
print("x Exit")
entry = input("> ")
num2 = float(input("Enter second number: "))



# all variables in main
while entry != 'X' and entry !='x':
  if entry == "+":
    calculator.add(num1,num2)
    from calculator import answer
  elif entry == "-":
    calculator.subtract(num1,num2)
    from calculator import answer
  elif entry == "*":
    calculator.multiply(num1,num2)  
    from calculator import answer
  elif entry == "/":
    calculator.divide(num1,num2)
    from calculator import answer
  elif entry == "^":
    calculator.pow(num1,num2)
    from calculator import answer
  elif entry == "i" or "I":
    calculator.invert(num1,num2) 
    from calculator import answer
  elif entry == "s" or "S":
    calculator.save(num1,num2) 
    from calculator import answer
  elif entry == "r" or "R":
    calculator.recall(num1,num2) 
    from calculator import answer
  elif entry == "c" or "C":
    calculator.memClear(num1,num2) 
    from calculator import answer
  else:
    print("Invalid input.")          
  
  num1 = answer
  entry = input(print("> ")) 
  num2 = float(input("Enter second number: "))   
  if entry != "x" or "X":
      continue

