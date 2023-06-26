print("Hello Jenkins")

# Basic Arithmetic Calculator

numberOne = int(input("Enter The Number: "))
Operand0 = input("Enter The following of operators only one : +,-,/,*: ")

numberTwo = int(input("Enter The Number: "))

if Operand0 == "*":
    print(numberOne, "*", numberTwo, "=", numberOne * numberTwo)
elif Operand0 == "+":
    print(numberOne, "+", numberTwo, "=", numberOne + numberTwo)
elif Operand0 == "-":
    print(numberOne, "-", numberTwo, "=", numberOne - numberTwo)
elif Operand0 == "/":
    print(numberOne, "/", numberTwo, "=", numberOne / numberTwo)
else:
    print("Invalid Operand")

