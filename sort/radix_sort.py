# coding: utf-8

def _sort(arr, new_arr, mask, shift, num):
	m = len(arr)
	count = [0] * num
	for i in range(m):
		count[(arr[i] >> shift) & mask] += 1
	for i in range(1, num):
		count[i] += count[i-1]
	for i in range(m-1, -1, -1):
		val = (arr[i] >> shift) & mask
		count[val] -= 1
		new_arr[count[val]] = arr[i]


def radix_sort(arr):
	"""radix sort, for interger sort"""
	new_arr = [0] * len(arr)
	_sort(arr, new_arr, 0xFF, 0, 256)
	_sort(new_arr, arr, 0xFF, 8, 256)
	_sort(arr, new_arr, 0xFF, 16, 256)
	_sort(new_arr, arr, 0xFF, 24, 256)

if __name__ == '__main__':
	import random
	arr = [random.randrange(1000) for i in range(15)]

	sorted_arr = arr[:]
	radix_sort(sorted_arr)
	print arr
	print sorted_arr