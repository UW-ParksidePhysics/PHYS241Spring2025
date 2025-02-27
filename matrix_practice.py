import numpy as np


matrix_A = np.array([[1, 2], [3, 4]])
print(f'A = {matrix_A}')

matrix_B = np.array([[5, 6], [7, 8]])
print(f'B = {matrix_B}')

print(f'A + B  = {matrix_A + matrix_B}')
print(f'A - B  = {matrix_A - matrix_B}')

print(f'A B = {np.matmul(matrix_A, matrix_B)}')

# list_C = [i for i in range(1, 5)]
list_C = list(range(1, 5))
matrix_C = np.array(list_C).reshape(2, 2)
print(f'C = {matrix_C}')