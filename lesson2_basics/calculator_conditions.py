#input
num1 = int(input("Pick first number: "))
num2 = int(input("Pick second number: "))
operation = input ("Choose an operations: add, subtract, multiply or divide: ")

#operation
if operation == "add": 
    print(f"{num1 + num2}")
elif operation == "subtract":
        print(f"{num1 - num2}")
elif operation == "multiply":
        print(f"{num1 * num2}")
else:
        print(f"{num1 / num2}")
