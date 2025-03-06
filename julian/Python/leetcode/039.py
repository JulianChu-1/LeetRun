from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(state, target, choices, start, res):
            if target == 0:
                res.append(list(state))
                return

            for i in range(start, len(choices)):
                if target - choices[i] < 0:
                    break

                state.append(choices[i])
                backtrack(state, target - choices[i], choices, i, res)
                state.pop()
        
        state = []
        candidates.sort()
        start = 0
        res = []
        backtrack(state, target, candidates, start, res)

        return res