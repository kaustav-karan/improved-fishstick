import Addition
import Subtraction
import Division
import Multiplication
import Increment
import Decrement

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Increment")
print("7. Decrement")

operation = input("Enter choice (1/2/3/4/5/6/7): ")

match operation:
    case '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) 
        result = Addition.add(num1, num2)
        print(f"The result of addition is: {result}")
    case '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) 
        result = Subtraction.subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
    case '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) 
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    case '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) 
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero.")
    case '5':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter raise to: ")) 
        result = num1 ** num2
        print(f"The result of power is: {result}")
    case '6':
        num1 = float(input("Enter number: "))
        result = Increment.increment(num1)
        print(f"The result of increment is: {result}")
    case '7':
        num1 = float(input("Enter number: "))
        result = Decrement.decrement(num1)
        print(f"The result of decrement is: {result}")
    case _:
        print("Invalid input! Please select a valid operation.")