from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        set_m = set()
        set_n = set()

        for i in range(m):
            for j in range(n):
                if matrix[m][n] == 0:
                    set_m.add(m)
                    set_n.add(n)

        for i in range(m):
            for j in range(n):
                if i in set_m or j in set_n:
                    matrix[i][j] = 0