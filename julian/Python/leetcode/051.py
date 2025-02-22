from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chessboard = [['.'] * n for _ in range(n)]

        def isValid(n, row, col, chessboard):
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(n : int, row : int, chessboard : List[List[str]]):
            if row == n:
                temp_res = []
                for temp in chessboard:
                    temp_str = ''.join(temp)
                    temp_res.append(temp_str)
                res.append(temp_res)
                return
            
            for col in range(n):
                if isValid(n, row, col, chessboard):
                    chessboard[row][col] = 'Q'
                    backtrack(n, row + 1, chessboard)
                    chessboard[row][col] = '.'

        backtrack(n, 0, chessboard)
        
        return res


s = Solution()
print(s.solveNQueens(4))