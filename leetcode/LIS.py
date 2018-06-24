# coding: utf-8

def LIS(arr):
	"""naive dp"""
	m = len(arr)
	if m <= 1:
		return m

	dp = [1] * m
	res = 0
	for i in range(1, m):
		n = 0
		for j in range(0, i):
			if arr[j] < arr[i]:
				n = max(dp[j], n)
		dp[i] = n + 1
		res = max(dp[i], res)

	return res

def LIS2(arr):
	"""dp with binary search"""
	def binary_search(arr, b, e, num):
		while b < e:
			mid = b + (e - b) / 2
			if arr[mid] == num:
				return mid
			elif arr[mid] < num:
				b = mid + 1
			else:
				e = mid

		return b

	m = len(arr)
	if m <= 1:
		return m

	dp = [0] * m  # dp[i], smallest value LIS with length of i ends with
	res = 1
	dp[0] = arr[0]
	for i in range(1, m):
		idx = binary_search(dp, 0, res, arr[i])
		dp[idx] = arr[i]
		res = max(idx + 1, res)

	return res


if __name__ == '__main__':
	test_cases = [
		[],
		[2],
		[2,4,5,6,7,8],
		[7,6,5,3,2],
		[1,5,2,64,2,34,5,354,6467,5342,33,34,56,343],
	]

	for test_case in test_cases:
		print LIS(test_case), LIS2(test_case)