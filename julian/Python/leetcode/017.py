from typing import List

phone = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        
        def backtrack(conbination, nextdigits):
            if len(nextdigits) == 0:
                res.append(conbination)
            
            else:
                for digit in phone[nextdigits[0]]:
                    backtrack(conbination + digit, nextdigits[1:])
            
        backtrack('', digits)

        return res
    
    def lettter2(self, digits):
        if not digits: return []
        n = len(digits)
        res = []
        path = [''] * n

        def backtrack(i):
            if i == n:
                res.append(''.join(path))
                return
            
            for c in phone[digits[i]]:
                path[i] == c
                backtrack(i + 1)
        
        backtrack(0)

        return res
