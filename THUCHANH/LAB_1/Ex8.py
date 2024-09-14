def mProd(A, B):
    # Check if the matrices have compatible dimensions for multiplication
    if len(A[0]) != len(B):
        print("Matrix dimension error")
        return None

    # Get the dimensions of the matrices
    m = len(A)
    n = len(A[0])
    q = len(B[0])

    # Initialize the result matrix C
    C = [[0] * q for _ in range(m)]

    # Calculate the product of matrices A and B
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = mProd(A, B)
if C is not None:
    print("Result matrix C:")
    for row in C:
        print(row)