from numpy import array, arange,vstack,dot,random
from matplotlib import pyplot as p

# 3x3 matrix
first_matrix=arange(3,12)
first_matrix=first_matrix.reshape([3,3])
print first_matrix

# Display minimum, maximum and mean of all entries 
print "\n min: ",first_matrix.min()

print "\nmax: ",first_matrix.max()

print "\nmean: ",first_matrix.mean()

#Square every entry in first_matrix
second_matrix=first_matrix**2

# stack first_matrix on top of second_matrix

third_matrix=vstack([first_matrix,second_matrix])
print"\n Third_matrix:\n\n", third_matrix
#  dot() to calculate the dot product of third_matrix by first_matrix
print"dot_matrix: ",dot(third_matrix,first_matrix)
# Reshape third_matrix into an array of dimensions 3 x 3 x 2
print third_matrix.reshape(3,3,2)


