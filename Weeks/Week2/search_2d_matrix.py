class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row_ind = 0
        start, end = 0, len(matrix) - 1
        while start <= end:
            mid = (start + end) // 2
            row = matrix[mid]
            if row[0] <= target:
                row_ind = mid
                start = mid + 1
            elif row[0] > target:
                end = mid - 1

        start, end = 0, len(matrix[row_ind]) - 1
        while start <= end:
            mid = (start + end) // 2
            val = matrix[row_ind][mid]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            elif val > target:
                end = mid - 1
        else:
            return False
