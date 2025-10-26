class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, down = 0, len(matrix) - 1
        tmp = []
        while top <= down:
            mid = (top + down) // 2
            tmp = matrix[mid]
            left, right = 0, len(tmp) -1
            while left <= right:
                m = (left + right) // 2
                if tmp[m] == target:
                    return True
                else:
                    if tmp[m] < target:
                        left = m + 1
                    else:
                        right = m - 1
            if matrix[mid][-1] < target:
                top = mid + 1
            else:
                down = mid - 1
        return False
