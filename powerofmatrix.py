#CALCULATING POWER OF MATRIX using Numpy
import numpy as np
from numpy.linalg import matrix_power
from numpy.linalg import multi_dot
from numpy import *
#--------------------------------------------------------------------------EXAMPLE 1 (2*2 matrix)
print("-----EXAMPLE 1-----")
A=np.random.randint(10,size=(2,2))
answer=np.linalg.matrix_power(A,2)
print("answer 1 : " ,answer)

#--------------------------------------------------------------------------EXAMPLE 2 ((3*3 matrix))
print("-----EXAMPLE 2-----")
B=np.random.randint(10,size=(2,3,2,2))
#print(A
print(B)
print("----------")
answer_=np.linalg.matrix_power(B,2)
print("answer 2a : " ,answer_)

#EXTRA EXAMPLE
B=np.random.randint(10,size=(4,2,2,2))

print(B)
print("----------")
answer_=np.linalg.matrix_power(B,2)
print("answer 2b: " ,answer_)

#--------------------------------------------------------------------------EXAMPLE 3(3*3 matrix)
print("-----EXAMPLE 3  have errors-----")

C=np.random.randint(10,size=(2,2,3))   #rows and column unmatch

print(B)
"""The number of columns of the 1st matrix must equal the number of rows of the 2nd matrix.
And the result will have the same number of rows as the 1st matrix, and the same number of columns as the 2nd matrix."""
answer_=np.linalg.matrix_power(C,2)
print("answer 3 : " ,answer_)
