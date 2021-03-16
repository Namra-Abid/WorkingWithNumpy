
import numpy as np
# Example 1 - working
a = np.array([[7,8,9],[4,1,2]])

print ('First array:' )
print (a)
print ('\n')

print ('Append elements to array:' )
print (np.append(a, [3,0,9]))

# Example 2 - working
a = np.array([[7,8,9],[4,1,2]])

print ('First array:' )
print (a)
print ('\n')
print ('Append elements along axis 0:' )
print( np.append(a, [[3,0,9]],axis = 0) )

#Example 3 -breaking


a = np.array([[7,8,9],[4,1,2]])

print ('First array:' )
print (a)
print ('\n')
print ('Append elements along axis 0:' )
print( np.append(a, [[4,4,4]],axis = 0) )
