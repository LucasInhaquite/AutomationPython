# For Loop with increment value
# (Initial value, final value, increment value)
# Ex (1,11,2) it will print 1,3,5,7,9 the 11 it's not considered as it is the last number

number = input("Please enter your number = ")

for i in range (10,0,-1):
    if (int(number) * i % 10 == 0):
        continue
    print(int(number)*i)
else:11
print("Loop is ended")