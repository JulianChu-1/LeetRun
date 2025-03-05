from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = collections.defaultdict(int)
        cnt[0] = 1

        def dfs(root, cur):
            if not root: return 0

            ret = 0
            cur += root.val
            ret += cnt[cur - targetSum]
            cnt[cur] += 1
            ret += dfs(root.left, cur)
            ret += dfs(root.right, cur)
            cnt[cur] -= 1

            return ret
        
        return dfs(root, 0)
    
    def easyOne(self, root, targetSum):
        def rootSum(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)
            return ret
        
        if root is None:
            return 0
            
        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret


            
