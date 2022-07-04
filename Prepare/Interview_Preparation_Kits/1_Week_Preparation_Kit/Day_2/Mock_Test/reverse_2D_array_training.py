

#
# this code is used to manipulate 2D array by either reversing columns or reversing rows
#
#
#  https://www.youtube.com/watch?v=YWbBFOsN7I0	
#
#  EXAMPLE:

#creare 2D array with 4 rows and 5 columns


#	11 17 13 15 19 18  # 4 as, 8 bs, 8 cs, 16 ds
#	20 23 25 27 29 21
#	31 33 35 37 39 32
#	48 41 43 45 47 49
#   51 53 55 58 52 59
#   64 60 63 67 69 61
#
#
#	11 17 13    # 1 a, 2 bs, 2 cs, 4 ds
#	20 23 25 
#	31 33 35
#
#
#  

array=[[11,17,13,15,19,18],[20,23,25,27,29,21],[31,33,35,37,39, 32],[48, 41,43,45,47,49],[51, 53, 55,58, 52, 59],[64, 60, 63, 67, 69, 61]]
	

def column(a, i, start_row, end_row):


	c = [0]*(end_row - start_row)

	row_pos = start_row
	print(start_row)
	for x in range(0, len(c)):

		c[x] = a[row_pos][i]
		row_pos += 1

	return c

def reverseMatrix(arr):

	n = int(len(arr) / 2)
	a_s  = 4
	b_s = (2*n -2)*2
	c_s = (2*n -2)*2
	d_s = (2*n -2)*4

	a_s_tc = 1
	b_s_tc = (n -2)*2
	c_s_tc = (n -2)*2
	d_s_tc = (n -2)*4

	print("")
	print(a_s)
	print(b_s)
	print(c_s)
	print(d_s)

	print("")
	print(a_s_tc)
	print(b_s_tc)
	print(c_s_tc)
	print(d_s_tc)

	a_arr = [0]*a_s
	b_arr = [0]*b_s 
	c_arr = [0]*c_s 
	d_arr = []

	# construct a_arr

	a_arr[0]= arr[0][0]
	a_arr[1]= arr[0][len(arr[0]) - 1] 
	a_arr[2]= arr[len(arr)-1][0]
	a_arr[3]= arr[len(arr)-1][len(arr[0])-1]

	# construct b_arr 

	b_arr = arr[0][1 : int(b_s/2)+1 ] 
	b_arr += arr[len(arr)-1][1 : int(b_s/2)+1 ] 


	# construct c_arr 

	c_arr = column(arr, 0, 1, len(arr)-1)
	c_arr += column(arr, len(arr) -1, 1, len(arr)-1)

	# construct d_arr

	for i in range(1, len(arr)-1):
		d_arr += arr[i][1:len(arr)-1]



	print("")
	print(a_arr)
	print("")
	print(b_arr)
	print("")
	print(c_arr)
	print("")
	print(d_arr)

	a_arr.sort()
	a_arr = a_arr[::-1]
	a_arr = a_arr[0:a_s_tc]

	print("")
	print(a_arr)

	b_arr.sort()
	b_arr = b_arr[::-1]
	b_arr = b_arr[0:b_s_tc]

	print("")
	print(b_arr)

	c_arr.sort()
	c_arr = c_arr[::-1]
	c_arr = c_arr[0:c_s_tc]

	print("")
	print(c_arr)

	d_arr.sort()
	d_arr = d_arr[::-1]
	d_arr = d_arr[0:d_s_tc]

	print("")
	print(d_arr)

	result_arr = a_arr + b_arr + c_arr + d_arr

	print("")
	print(result_arr)

	print("")
	print(sum(result_arr))

	return sum(result_arr)
	

print("")
print(array)


reverseMatrix(array)


