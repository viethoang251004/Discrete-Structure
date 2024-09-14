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
    # Perform the operation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '^':
        result = num1 ** num2
    else:
        print("Invalid operator")
        return
    print("Result:", result)

# Example usage
calculate_operation()