num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
num3 = input("Please enter the third number: ")

if((num1>num2)&(num1>num3)):
    print(num1," is greatest number")
elif((num2>num3)&(num2>num1)):
     print(num2," is greatest number")
else:
     print(num3," is greatest number")
