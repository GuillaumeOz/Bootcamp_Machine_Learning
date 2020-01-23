#!/usr/bin/python3

import numpy as np

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])

X2 = np.array([[1], [2], [3], [5], [8]])
theta2 = np.array([[2.]])

X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,80.]])
theta3 = np.array([[0.05], [1.], [1.], [1.]])

def predict_(theta, X):

if __name__ == "__main__":
	print(theta1.shape)
	print(X1.shape)
	print()
	print(theta2.shape)
	print(X2.shape)
	print()
	print(theta3.shape)
	print(X3.shape)

# % The ; denotes we are going back to a new row.
# A = [1, 2, 3; 4, 5, 6; 7, 8, 9; 10, 11, 12]

# % Initialize a vector 
# v = [1;2;3] 

# % Get the dimension of the matrix A where m = rows and n = columns
# [m,n] = size(A)

# % You could also store it this way
# dim_A = size(A)

# % Get the dimension of the vector v 
# dim_v = size(v)

# % Now let's index into the 2nd row 3rd column of matrix A
# A_23 = A(2,3)