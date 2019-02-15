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
def invert(answer):
    return 0.0 - answer

# This function saves answer
def save(answer, mem):
    answer = mem
    return 0

# This function recalls memory
def recall(mem, answer):
    mem = answer
    return 0

# This function clears memory
def memClear(mem):
    mem = 0
    return 0