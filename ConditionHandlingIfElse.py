i = 10

# Check number is greater then 100 then print "GREATER"
# Else number is Smaller

inputNumber = input("Please digit your number --> ")

# All inputs from users are stored as String so we need to cast the value as int to use numeric operators

if (int (inputNumber) > 100):
    print("Number is Greater")
else:
    print("Number is Smaller")
