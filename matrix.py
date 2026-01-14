#!/usr/bin/python3

import numpy as np

class MyMatrix:
    """
    Operations on matrices
    """

    def __init__(self, n):
        self.data = np.random.rand(n, n)

    def shape(self):
        return self._a.shape

    def __add__(self, other):
        return self.data + other.data

    def __mul__(self, other):
        return np.matmul(self.data, other.data)

    def inverse(self):
        return np.linalg.inv(self.data)

    def eigenvalues(self):
        return np.linalg.eigvals(self.data)
    
    def determinant(self):
        return np.linalg.det(self.data)

    def __str__(self):
        return np.array2string(self.data, precision=3)

if __name__ == "__main__":
    N = 4
    matrix1 = MyMatrix(N)
    matrix2 = MyMatrix(N)

    print(matrix1.inverse())
    print(matrix1.determinant())
    print(matrix1.eigenvalues())
    print(matrix1 + matrix2)
    print(matrix1 * matrix2)

