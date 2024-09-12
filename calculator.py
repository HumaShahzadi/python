# assignment 6
def calculator():
    # Taking input from the user for the operation
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Validating user input
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please try again.")
        return
    
    # Taking input for the numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return
    
    # Performing the operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of division is: {result}")

# Calling the calculator function
calculator()