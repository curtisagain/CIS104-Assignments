answer = 0
mem = 0
# This function adds two numbers 
def add(num1, num2):
   answer = num1 + num2
   return print(answer)

# This function subtracts two numbers 
def subtract(num1, num2):
   answer = num1 - num2
   return print(answer)
# This function multiplies two numbers
def multiply(num1, num2):
   answer = num1 * num2
   return print(answer)

# This function divides two numbers
def divide(num1, num2):
   answer = num1 / num2
   return print(answer)
        # https://www.programiz.com/pnum2thon-programming/examples/calculator

# This function finds the power
def pow(num1, num2):
    answer = num1 ** num2
   return print(answer)

# This function inverts answer
def invert(answer):
    answer = 0.0 - answer
    return print(answer)

# This function saves answer
def save(answer, mem):
    answer = mem
    return print(mem)

# This function recalls memory
def recall(mem, answer):
    mem = answer
    return print(answer)

# This function clears memory
def memClear(mem):
    mem = 0
    return print("Memory Cleared.")