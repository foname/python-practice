
def swap(left, right):
	return right, left

def randomString(strLen):
	from random import shuffle
	a = [ i for i in range(0, strLen)]
	shuffle(a)
	return a

def quickSort(input):
	# print "input: {}".format(input)
	inputLen = len(input)
	if inputLen == 1:
		return input
	elif inputLen == 2 and input[0] > input[1]:
		input[0], input[1] = swap(input[0], input[1])
		return input
	# setup pivot, left-right index
	pivot = input[inputLen-1]
	lIndex = 0
	rIndex = inputLen-2
	left = input[lIndex]
	right = input[rIndex]
	# print "index: {}, {}".format(lIndex, rIndex)
	while lIndex <= rIndex:
		while input[lIndex] <= pivot:
			if (lIndex-rIndex) >= 0:
				break;
			lIndex = lIndex+1
		while input[rIndex] >= pivot:
			if (lIndex-rIndex) >= 0:
				break;
			rIndex = rIndex-1

		# print "break at : pivot: {}, left: {}, right: {}".format(pivot, input[lIndex], input[rIndex])
		input[lIndex], input[rIndex] = swap(input[lIndex], input[rIndex])
		# print "swapped : pivot: {}, left: {}, right: {}".format(pivot, input[lIndex], input[rIndex])
		# print "list changed: {}".format(input)
		# print "current index {}, {}".format(lIndex, rIndex)
		# if (rIndex-lIndex) <= 1:
		# print "{}, {}".format(input[rIndex], pivot)
		if input[rIndex] > pivot and (rIndex-lIndex) <= 1:
			input[rIndex], input[inputLen-1] = swap(input[rIndex], input[inputLen-1])
		lIndex = lIndex+1
		rIndex = rIndex-1
		# print "{} > {}?".format(input[lIndex], pivot)
		# if input[lIndex] > pivot:
		
	# print "last lindex {}, last rindex {}".format(lIndex, rIndex)
	# print "final list {}".format(input)
	# print input[:lIndex]
	# print input[lIndex:]
	return quickSort(input[:lIndex]) + quickSort(input[lIndex:])
	# return

def main():

	# left, right = swap(1, 0)
	# print "left : {}" .format(left)
	# print "right : {}".format(right)
	input = randomString(10)
	# input = [54,26,93,17,77,31,44,55,20]
	# input = [26, 54, 77, 31, 44, 55]
	# input = [26, 54, 44, 31]
	print "original list : {}".format(input)
	output = quickSort(input)
	print output
	

if __name__ ==	 "__main__":
	main()
