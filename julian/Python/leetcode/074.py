from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = -1, m * n

        while left + 1 < right:
            mid = (left + right) // 2
            x = matrix[mid // n][mid % n]

            if x == target:
                return True
            elif x < target:
                left = mid
            else:
                right = mid
        
        return False
    
    def easy(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:  # 还有剩余元素
            if matrix[i][j] == target:
                return True  # 找到 target
            if matrix[i][j] < target:
                i += 1  # 这一行剩余元素全部小于 target，排除
            else:
                j -= 1  # 这一列剩余元素全部大于 target，排除
        return False
