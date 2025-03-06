from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if board[i][j] != word[k]: 
                return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < row and 0 <= y < col and backtrack(x, y, k + 1):
                    return True
            
            board[i][j] = word[k]
            return False

        row = len(board)
        col = len(board[0])
        
        return any(backtrack(i, j, 0) for i in range(row) for j in range(col))
