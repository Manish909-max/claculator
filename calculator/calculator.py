print("1- Addition")
print("2- Subtract")
print("3- Multiplication")
print("4- Division")
option = int(input("choose the operation you wnt to do: "))


if(option in[1,2,3,4]):
    num1 = int(input("enter the first number"))
    num2 = int(input("enter the second number"))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2

else:
    print("invalid operation")


print("the result of the operation is {}".format(result))
