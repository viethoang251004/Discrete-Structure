def process_string():
    A = input("Input your string: ")
    # Remove spaces
    B = A.split()
    result_no_space = ''.join(B)
    # Replace spaces with underscores
    result_with_underscore = '_'.join(B)
    print("Result without space:", result_no_space)
    print("Result with underscore:", result_with_underscore)

# Example usage
process_string()