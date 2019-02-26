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
print("m Clear Memory")
print("c Clear")
print("x Exit")
entry = input("> ")
# Like a do while loop in python
while True :
  if (entry == "+" or entry == "-" or entry == "*" or entry == "/" or entry == "^"):
    
    num2 = float(input("Enter second number: "))
  
    if entry == "+":
      answer = calculator.add (num1,num2)
      num1 = answer
      print (answer)
      entry = input("> ")
  
    elif entry == "-":
      answer = calculator.subtract (num1,num2)
      num1 = answer
      print (answer)
      entry = input("> ")
  
    elif entry == "*":
      answer = calculator.multiply (num1,num2)  
      num1 = answer
      print (answer)
      entry = input("> ")

    elif entry == "/":
      answer = calculator.divide (num1,num2)
      num1 = answer
      print (answer)
      entry = input("> ")

    elif entry == "^":
      answer = calculator.pow(num1,num2)
      num1 = answer
      print (answer)
      entry = input("> ")
    # user errors
    else:
      print("Invalid input.")
  
  elif (entry != "+" or entry != "-" or entry != "*" or entry != "/" or entry != "^"):
    if (entry == "i" or entry == "I"):
      answer = calculator.invert(num1) 
      num1 = answer
      print (answer)
      entry = input("> ")
  
    elif (entry == "m" or entry == "M"):
      calculator.memClear() 
      print ("Memory cleared.")
      print (answer)
      entry = input("> ")
  
    elif (entry == "c" or entry == "C"):
      calculator.clear(num1) 
      num1 = float(input("Cleared. Enter first number: "))
      entry = input("> ")
 
    elif (entry == "s" or entry == "S"):
      calculator.save(answer) 
      num1 = float(input("Saved. Enter first number: "))
      entry = input("> ")

    elif (entry == "r" or entry == "R"):
      answer = calculator.recall(num1) 
      num1 = answer
      print ("Recalled.")
      print (answer)
      entry = input("> ")

    if entry != "x" or "X":
      continue          