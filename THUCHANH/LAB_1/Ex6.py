def calculate_operation():
    input_str = input("Input your operation: ")
    # Split the input string into three substrings: first number, operator, second number
    input_list = input_str.split()
    if len(input_list) != 3:
        print("Invalid input format")
        return
    num1 = int(input_list[0])
    operator = input_list[1]
    num2 = int(input_list[2])
    # Define a dictionary to map operators to corresponding functions
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y,
        '^': lambda x, y: x ** y
    }
    # Check if the operator is valid
    if operator not in operations:
        print("Invalid operator")
        return
    # Perform the operation using the corresponding function from the dictionary
    result = operations[operator](num1, num2)

    print("Result:", result)

# Example usage
calculate_operation()