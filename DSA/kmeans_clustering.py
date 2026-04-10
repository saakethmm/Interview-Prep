from typing import List 
import math

def min_distance_from_cluster(points: List, k: int):
	"""
	greedy + binary search
	O(NlogD)
	"""
	# binary search (on the answer, becaue the solution is monotonic!) 
	# + greedy (to check feasibility of each binary search check)...

	points.sort()
	start, end = 0, math.ceil((points[-1] - points[0]) / 2)
	best_so_far = end
	mid =  (end + start) // 2

	# O(N) where N number of pts
	def check_distance(m):
		"""
		greedy check
		"""
		c_idx = 0
		c_start, c_end = 0, 0
		while k - 1 - c_idx >= 0:
			if points[c_end] - points[c_start] <= 2 * m:
				c_end += 1
				if c_end == len(points):
					return True
			else:
				c_idx += 1
				c_start = c_end
		return False

	# tested set
	tested = set()

	# standard binary search with different check
	# log of max distance
	while mid not in tested:
		tested.add(mid)
		if check_distance(mid):
			best_so_far = mid
			end = mid
		else:
			start = mid
		mid = (start + end) // 2

	return best_so_far

if __name__ == '__main__':
	test_arr = [-5, 1, 4, 6, 7]
	k = 3
	print(min_distance_from_cluster(test_arr, k))






	