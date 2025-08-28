class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search across rows first to pick right row
        lower_row = 0
        upper_row = len(matrix)

        while lower_row < upper_row:
            mid_row = (lower_row + upper_row) // 2
            print(matrix[mid_row][0])
            if target < matrix[mid_row][0]:
                # break out of loop if unchanged
                if upper_row == mid_row:
                    break
                upper_row = mid_row
            else:
                # break out of loop if unchanged
                if lower_row == mid_row:
                    break
                lower_row = mid_row

        print(f'Reached: {mid_row}')
        # binary search across cols of selected row
        lower = 0
        upper = len(matrix[0])

        while lower < upper:
            mid = (lower + upper) // 2
            if target == matrix[mid_row][mid]:
                return True
            elif target < matrix[mid_row][mid]:
                if upper == mid:
                    break
                upper = mid
            else:
                if lower == mid:
                    break
                lower = mid
        
        return False
        
        
