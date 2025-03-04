from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder = []

        def preorderTra(root : TreeNode):
            if root:
                preorder.append(root)
                preorderTra(root.left)
                preorderTra(root.right)

        preorderTra(root)
        for i in range(1, len(preorder)):
            pre, cur = preorder[i - 1], preorder[i]
            pre.left = None
            pre.right = cur
    
    def fla(self, root):
        preorder = []

        def preorderTra(root : TreeNode):
            stack = [root]

            while stack:
                node = stack.pop()
                preorder.append(node)
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)

        preorderTra(root)
        for i in range(1, len(preorder)):
            pre, cur = preorder[i - 1], preorder[i]
            pre.left = None
            pre.right = cur