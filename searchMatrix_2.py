class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        i = len(matrix)
        j = 0
        while j < i:
            left, right = 0, len(matrix[j]) -1
            while left <= right:
                mid = (left + right) // 2
                if matrix[j][mid] == target:
                    return True
                else:
                    if matrix[j][mid] < target:
                        left = mid + 1
                    else:
                        right = mid -1
            j += 1
        return False
