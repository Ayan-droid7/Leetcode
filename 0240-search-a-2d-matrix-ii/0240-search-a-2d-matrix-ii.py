from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix[0])

        
        for row in matrix:
           
            left, right = 0, n - 1
            first_true_index = -1

            while left <= right:
                mid = (left + right) // 2
                if row[mid] >= target:
                    first_true_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

           
            if first_true_index != -1 and row[first_true_index] == target:
                return True

     
        return False
