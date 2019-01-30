title = input("Enter Title. ")
author = input("Enter Author. ")
year = int(input("Enter year published. "))
pages = int(input("Enter pagecount. "))

bookAge = 2019 - year
if (bookAge < 10):
    print("This book is younger than ten years old.")
else:
    print("This book is at least ten years old")

if (pages < 100):
    print("This book is a short book")
elif (pages >= 100) & (pages <= 300):
    print("This book is an average book.")
else:
    print("This is a long book.")