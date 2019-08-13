# Take 1 number from user

inputNumber = input("Please enter your number: - ")
inputNumber=int(inputNumber)


if (inputNumber>=0):
    if(inputNumber%2==0):
        print("This number is Even")
    else:
        print("This number is Odd")
else:
    print("This number is negative")