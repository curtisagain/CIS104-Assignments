import msvcrt as m
from calculator import calculate
print(">")
entry = ""
op = ("+", "-", "*", "/", "^")
calcFunc = ("s", "S", "c", "C", "r", "R", "m", "M")
num1 = 0
num2 = 0
answer = 0
# all variables in main
while entry != 'X' and entry !='x':
    entry = str(m.getch().decode("utf-8"))
    #utf-8 is a declaration of unicode entry, from basilije in cpp class
    if (entry != op) & (entry != calcFunc):
        entry = num1




print("Goodbye.")