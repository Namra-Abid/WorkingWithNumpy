import numpy as np
data = [1,2,3,4,5]
first_quartile = np.quantile(data, 0.25)
#print(first_quartile)

# Example 1- working
data = [1,2,3,4,5]
first_quartile = np.quantile(data, 0.5)
print(first_quartile)
"""
Above, we can see a straightforward example of the quantile. Here we are dealing with a four-group quantile, also called quartile.
At first, we have imported the NumPy module. Then, they declared a 1-d array.
After which, we have used our syntax and print statement to get the desired output.
Like any other statical operation, first, our data is arranged in a particular order, usually ascending. After which the operation is performed.
"""

# Example 2- working
a = np.array([[10, 7, 4], [3, 2, 1],[5,6,8],[9,0,0]])

print(np.quantile(a, 0.5))
"""
In the above example, we have considered a 2-dimensional array.
Rest we have followed all the steps the same as the first example. Here we are dealing with a 12 group
first arrange them 0,0,1,2,3,4,5,6,7,8,9,10
centre values are 4 and 5 therefore ,(4+5)/2=4.5
"""
a=[[1,23,4,5,6],
   [2,45,5,6,7]]

print(np.quantile(a,.50,axis=1))
"""
we have defined the axis as 1, so we get quantile value separately for the 2 sub-arrays.
1st sub array  : [1,23,4,5,6] ----> after arranging it [1,4,5,6,23]--- mid value 5
2nd sub array  : [2,45,5,6,7] ----> after arranging it [2,5,6,7,45]--- mid value 6
"""

# Example 3 - breaking (to illustrate when it breaks)
a = np.array([[3, 2, 1,4], [2,5]])
print(np.quantile(a, 0.5, axis=0))
""" In the above example, since axis = 0, hence the quantile will be calculated rowwise,
 but since both the arrays have unequal element hence we got the error due to missing element in the second array.
  To fix this please pass arrays with equal length while calculating quantile rowwise.
This function can be used to find the meadian of an array
and also the min value and max value by using the q = 0 and q = 1 respectively."""
