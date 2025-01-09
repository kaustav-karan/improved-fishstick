print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

import Addition
import Subtraction
import Division
import Multiplication

operation = input("Enter choice (1/2/3/4/5): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: ")) 

if operation == '1':
    result = Addition.add(num1, num2)
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = Subtraction.subtract(num1, num2)
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error! Division by zero.")
elif operation == '5':
    result = num1 ** num2
    print(f"The result of power is: {result}")
else:
    print("Invalid input! Please select a valid operation.")