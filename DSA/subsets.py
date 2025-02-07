

N = 4

def search(k, curr_subset):
	if k == N:
		subsets.append(curr_subset)
		print(subsets[-1])
	else:
		search(k+1, curr_subset)
		curr_subset.append(k)
		search(k+1, curr_subset)
		curr_subset.pop()

if __name__ == '__main__':
	subsets = []
	search(0, [])
 


