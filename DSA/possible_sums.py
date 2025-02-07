# knapsack problem (dp)

def possible_sums(weights):
	total_sum = sum(weights)
	possible = [False] * (total_sum + 1)
	possible[0] = True
	for k in range(len(weights)):
		# descending order so that we don't use the same weight more than once (each outer loop iter is equivalent to each row in table)
		for i in range(total_sum, -1, -1):
			if possible[i]:
				possible[i + weights[k]] = True
	return possible

if __name__ == "__main__":
	print(possible_sums([1, 3, 3, 5]))

