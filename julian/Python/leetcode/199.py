from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
            
        stack = [root]

        while stack:
            res.append(stack[len(stack) - 1].val)
            level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            stack = level
        return res