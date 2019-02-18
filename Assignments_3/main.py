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
print("If using function i, s, r, c, or x, enter any value for second number.")
entry = input("> ")
num2 = float(input("Enter second number: "))



# all variables in main
while entry != 'X' and entry !='x':
  
  if entry == "+":
    answer = calculator.add (num1,num2)
    num1 = answer
    print (answer)
  
  elif entry == "-":
    answer = calculator.subtract (num1,num2)
    num1 = answer
    print (answer)
  
  elif entry == "*":
    answer = calculator.multiply (num1,num2)  
    num1 = answer
    print (answer)

  elif entry == "/":
    answer = calculator.divide (num1,num2)
    num1 = answer
    print (answer)

  elif entry == "^":
    answer = calculator.pow(num1,num2)
    num1 = answer
    print (answer)

  elif entry == "i" or "I":
    answer = calculator.invert(num1) 
    num1 = answer
    print (answer)
  
  elif entry == "c" or "C":
    answer = calculator.memClear(num1) 
    num1 = answer
    print ("Memory cleared.")
  
  elif entry == "s" or "S":
    answer = calculator.save(num1) 
    num1 = answer
    print (answer)

  elif entry == "r" or "R":
    answer = calculator.recall(num1) 
    num1 = answer
    print (answer)

  else:
    print("Invalid input.")          
  entry = input("> ") 
  num2 = float(input("Enter second number: "))   
  if entry != "x" or "X":
      continue

