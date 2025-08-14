from typing import List
from collections import defaultdict

def majorityElement(self, nums: List[int]) -> int:
    # approach 1
    # counts = defaultdict(int)
    # for num in nums:
    #     counts[num] += 1
    #     if counts[num] > len(nums) // 2:
    #         return num

    # approach 2
    nums.sort()
    return nums[len(nums) // 2]