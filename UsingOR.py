# Take 1 number from user
# Number is <0 or >100 display invalid

inputNumber = input("Please enter your number: - ")
inputNumber=int(inputNumber)

if(inputNumber<0 or inputNumber>100):
    print("This number is invalid")
else:
    print("This number is valid")