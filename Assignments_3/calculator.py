# This function adds two numbers 
def add(num1, num2):
   return num1 + num2

# This function subtracts two numbers 
def subtract(num1, num2):
   return num1 - num2

# This function multiplies two numbers
def multiply(num1, num2):
   return num1 * num2

# This function divides two numbers
def divide(num1, num2):
   return num1 / num2
        # https://www.programiz.com/pnum2thon-programming/examples/calculator

# This function finds the power
def pow(num1, num2):
    return num1 ** num2

# This function inverts answer
def invert(num1):
    return 0.0 - num1

# This function saves answer
def save(answer):
    global mem
    mem = answer
    return 0

# This function recalls memory
def recall(num1):
    global mem
    num1 = mem
    return (num1)

# This function clears memory
def memClear():
    global mem
    mem = 0
    return 0

    # This function clears the whole calculator
def clear(num1):
    global mem
    mem = 0
    num1 = 0
    return 0