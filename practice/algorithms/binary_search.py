from time import perf_counter_ns

def binary_search(arr, low, high, x):
	if low > high:
		return None

	middle = (high - low) // 2

	if arr[middle] == x:
		return middle

	if arr[middle] > x:
		return binary_search(arr, middle + 1, high, x)

	if arr[middle] < x:
		return binary_search(arr, low, middle - 1, x)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t1 = perf_counter_ns()
print(binary_search(nums, 0, len(nums) - 1, 50))
t2 = perf_counter_ns()
delta_t = t2 - t1

print(f'Binary search took {delta_t} ns')
