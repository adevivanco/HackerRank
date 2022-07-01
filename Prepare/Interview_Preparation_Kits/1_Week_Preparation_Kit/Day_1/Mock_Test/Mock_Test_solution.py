#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
	m = int(len(arr)/2)
	arr.sort()
	return str(arr[m])
