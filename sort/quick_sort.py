# coding: utf-8

def qsort(arr, start, end):
	if start >= end: 
		return

	m = start - 1
	pivot = arr[end]
	for i in range(start, end + 1, 1):
		if arr[i] <= pivot:
			m += 1
			arr[m], arr[i] = arr[i], arr[m]

	qsort(arr, start, m - 1)
	qsort(arr, m + 1, end)




if __name__ == '__main__':
	import random
	arr = [random.randrange(1000) for i in range(15)]

	sorted_arr = arr[:]
	qsort(sorted_arr, 0, len(sorted_arr) - 1)
	print arr
	print sorted_arr