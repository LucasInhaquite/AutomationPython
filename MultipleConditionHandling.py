# Taking one input
# Check if number is negative - Display number is negative, Check if number is 0 - Display number is 0
# Check if number is positive then check if is a Even number or an Odd number

inputNumber = input("Please enter your number -> ")
inputNumber = int(inputNumber)

if (inputNumber < 0):
    print("This is a negative number")
elif (inputNumber ==0):
    print("This is Zero")
elif (inputNumber%2==0):
    print("This number is an Even Number")
elif (inputNumber%2==1):
    print("This number is an Odd number")
else:
    print("Houston we have a problem")