age = int(input("Enter your age. "))
age = age + 10
print("In ten years, you'll be " + str(age) + " .")

degreesF = float(input("Enter the current temperature in degrees Fahreheit. "))
degreesC = (degreesF - 32) * 5 / 9
degreesC = round(degreesC, 3)
print("The current temperature in Celsius is" + str(degreesC) + " degrees.")