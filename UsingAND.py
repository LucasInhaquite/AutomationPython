# Take 1 number from user
# Number is positive and Divisible by 2 then the number is valid

inputNumber = input("Please enter your number: - ")
inputNumber = int(inputNumber)

if (inputNumber>=0 and inputNumber%2==0):
    print("This number is valid")
else:
    print("This number is invalid")
