import numpy as np
# Example 1 - working
a = np.arange(16).reshape(2,2,4)

print ('The original array is:' )
print (a)
print ('\n')

print('The transposed array is:')
print (np.transpose(a,(1,0,2)))
