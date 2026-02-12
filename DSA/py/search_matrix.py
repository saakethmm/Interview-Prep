from collections import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search across rows first to pick right row
        lower_row = 0
        upper_row = len(matrix) - 1

        while lower_row <= upper_row:  # always <= in case it's 1 element
            mid_row = (lower_row + upper_row) // 2
            # adjust upper_row down if target is smaller than smallest element in mid_row
            if target < matrix[mid_row][0]:
                upper_row = mid_row - 1
            # adjust lower_row up if target larger than largest element in mid_row
            elif target > matrix[mid_row][-1]:
                lower_row = mid_row + 1
            else:
                break

        # binary search across cols of selected row
        lower = 0
        upper = len(matrix[0]) - 1

        while lower <= upper:
            mid = (lower + upper) // 2
            if target == matrix[mid_row][mid]:
                return True
            elif target < matrix[mid_row][mid]:
                upper = mid - 1
            else:
                lower = mid + 1
        return False
        
        
