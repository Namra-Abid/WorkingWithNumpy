import numpy as np
# Example 1 - working
a = np.arange(9).reshape(3,3)

print ('The original array is:' )
print (a)
print ('\n')

print('The transposed array is:')
print (np.transpose(a))
#simple transpose
# Example 2- working
a = np.arange(16).reshape(2,2,4)
print("SHAPE")
print(a.shape) # shape is (2,2,4)
print ('The original array is:' )
print (a)
print ('\n')

print('The transposed array is:')
print (np.transpose(a,(1,0,2))) #value of shape at index position 0 and 1 are interchanged but as they are both same so no difference shape here is 2x2x4
print (np.transpose(a,(1,2,0)))# now shape chanes value at index 2 which is 4 become second value which means there will be 2 matrix each having 4 rows and 2 columns so shape is 2x4x2
 # Example 3 - breaking
a = np.arange(12).reshape(4,3)

print ('The original array is:' )
print (a)
print ('\n')

print('The transposed array is:')
print ( np.transpose(a,0))
