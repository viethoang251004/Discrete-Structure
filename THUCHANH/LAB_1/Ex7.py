def mSum(A, B):
    # Check if the matrices have the same dimensions
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrix dimension error")
        return None

    # Get the dimensions of the matrices
    m = len(A)
    n = len(A[0])

    # Initialize the result matrix C
    C = [[0] * n for _ in range(m)]

    # Calculate the summation of matrices A and B
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]

    return C

# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = mSum(A, B)
if C is not None:
    print("Result matrix C:")
    for row in C:
        print(row)