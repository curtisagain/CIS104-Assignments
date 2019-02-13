savedAnswer = 0


def add(num1, num2):
    inputNumber = (float(num1) + float(num2))
    
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def power(num1, num2):
    return num1 ** num2
def save(inputNumber):
    savedAnswer = inputNumber
def recall():
    return savedAnswer
def memClear():
    savedAnswer = 0
def invertSign(inputNumber):
    return 0.0 - inputNumber
