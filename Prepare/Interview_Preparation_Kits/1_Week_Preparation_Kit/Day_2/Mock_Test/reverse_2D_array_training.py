
#
#
# this code is used to manipulate 2D array by either reversing columns or reversing rows
#
# to reverse 
# to reverse a column create an array of the column to be reverse (i) first get the column_index, 
# (2) then iterate through the row index and swap the bottom row index with the top, (3) exit when
# the bottom is larger or equal to the top
#
#	array[row_index][column_index]= [values]
#
#	
#
#  EXAMPLE:

#creare 2D array with 4 rows and 5 columns


#	11 13 15 17 19
#	21 23 25 27 29
#	31 33 35 37 39
#	41 43 45 47 49

#  algorithm that tries all combinations

array=[[11,13,15,17,19],[21,23,25,27,29],[31,33,35,37,39],[41,43,45,47,49]]
	
def column1(matrix, i):
    return [row[i] for row in matrix]

def column2(matrix, i):
	c = [0]*len(matrix)

	for x in range(0, len(c)):
		c[x] = matrix[x][i]
	   
	return c


top = 0
bottom = len(array[0]) - 1  # get the number of columns to index rows

print(top)
print(bottom)

#while (bottom > top):
#	temp = array[1][top] 
#	array[1][top] = array[1][bottom]
#	array[1][bottom] = temp

#	bottom -= 1
#	top += 1

c = column1(array, 1)
print(c)

c2 = column2(array, 1)
print(c2)

print(array[0])


array[1].reverse()


print(array)