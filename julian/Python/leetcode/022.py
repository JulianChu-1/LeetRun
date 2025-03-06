from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        ans = []
        path = [''] * m

        def backtrack(i, open):
            if m == i:
                ans.append(''.join(path))
                return
            if open < n:
                path[i] = '('
                backtrack(i + 1, open + 1)
            if i - open < open:
                path[i] = ')'
                backtrack(i + 1, open)
        
        backtrack(0, 0)
        return ans