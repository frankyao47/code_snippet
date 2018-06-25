# coding: utf-8

def heapify(arr, m, idx):
	"""max_heap"""
	if idx < m:
		left, right = idx*2+1, idx*2+2
		pos, val = idx, arr[idx]
		if left < m and arr[left] > val:
			pos, val = left, arr[left]
		if right < m and arr[right] > val:
			pos, val = right, arr[right]
		if idx != pos:
			arr[idx], arr[pos] = arr[pos], arr[idx]
			heapify(arr, m, pos)

def build_heap(arr):
	m = len(arr)
	for i in range(m / 2, -1, -1):
		heapify(arr, m, i)

def heap_sort(arr):
	build_heap(arr)
	m = len(arr)
	for i in range(m):
		arr[m-i-1], arr[0] = arr[0], arr[m-i-1]
		heapify(arr, m-i-1, 0)
	

if __name__ == '__main__':
	import random
	arr = [random.randrange(1000) for i in range(15)]

	sorted_arr = arr[:]
	heap_sort(sorted_arr)
	print arr
	print sorted_arr