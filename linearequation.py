#LINEAR EQUATION SOLVE USING NUMPY

import numpy as np
"""  EXAMPLE 1
EQUATION -1
 2x +3y=8
 x+4y=9"""
# Example 1- working
print("-----------EXAMPLE 1--------")
a = np.array([[2,3],
     [1,4],
     ])
b= np.array([8,9])

x = np.linalg.solve(a, b)

print(x)
print("CHECKING: ",np.allclose(np.dot(a, x), b))

# Example 2- working
print("-----------EXAMPLE 2--------")
"""  EXAMPLE 2
EQUATION -2
 x+y-z=0
 2x-3y+z=1
 2x+y+z=7"""

c= np.array([[1,1,-1],
      [2,-3,1],
      [2,1,2]])
d= np.array([0,1,7])

y = np.linalg.solve(c, d)
print(y)
print("CHECKING: ",np.allclose(np.dot(a, x), b))

# Example 3- breaking
print("-----------EXAMPLE 3  have erros--------")
"""  EXAMPLE 2
EQUATION -2
 x+y-z=0
 2x-3y+z=1
"""

c= np.array([[1,1,-1],
      [2,-3,1],
     ])
d= np.array([0,1,7]) #there are three unknown variable so equation given must be 3 or value of atleast one varible should be told prior

y = np.linalg.solve(c, d)
print(y)
print("CHECKING: ",np.allclose(np.dot(a, x), b))
