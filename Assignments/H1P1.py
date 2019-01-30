
first_name = input('Please enter your first name:')
# saves input as variable
last_name = input('Please enter your last name:')
age = int(input('Please enter your age:'))
# using int converts string to integer to do maths
confidence = float(input('What is your confidence in programmers between 0-100%?'))
# floats don't have to be whole numbers
dog_age = (age * 7)
print('Hello', first_name, last_name, ', nice to meet you! You might be', age, 'in human years, but in dog years you are', dog_age,'.')
if (confidence/100) < .5: 
    print("I agree, programmers can't be trusted!")
else: 
    print("Writing good code takes hard work!")    