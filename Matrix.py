import numpy as np

# Create matrices
matrix_A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
matrix_B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])
# Addition
result_addition = matrix_A + matrix_B
print("Matrix Addition:")
print(result_addition)

# Subtraction
result_subtraction = matrix_A - matrix_B
print("\nMatrix Subtraction:")
print(result_subtraction)

# Multiplication (element-wise)
result_element_wise_multiplication = matrix_A * matrix_B
print("\nElement-wise Matrix Multiplication:")
print(result_element_wise_multiplication)

# Matrix multiplication
result_matrix_multiplication = np.dot(matrix_A, matrix_B)
print("\nMatrix Multiplication:")
print(result_matrix_multiplication)

# Transposition
transposed_matrix_A = np.transpose(matrix_A)
print("\nTransposed Matrix A:")
print(transposed_matrix_A)

# Determinant
determinant_A = np.linalg.det(matrix_A)
print("\nDeterminant of Matrix A:", determinant_A)

# Inverse
inverse_A = np.linalg.inv(matrix_A)
print("\nInverse of Matrix A:")
print(inverse_A)
