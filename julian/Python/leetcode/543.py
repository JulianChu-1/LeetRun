from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def depth(root):
            if not root:
                return 0
            L = depth(root.left)
            R = depth(root.right)

            self.ans = max(self.ans, L + R + 1)

            return max(L, R) + 1
        
        depth(root)

        return self.ans - 1