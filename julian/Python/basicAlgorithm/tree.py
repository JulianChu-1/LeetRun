class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):
        if value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def preorderTraversal(self):
        res = []

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(self.root)
        return res
    
    def preorderTraversal2(self):
        if not self.root:
            return []
        
        res = []
        stack  = [self.root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res
    
    def inorderTraversal(self):
        if not self.root:
            return []
        
        stack = []
        res = []
        root = self.root

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        
        return res
    
    def postorderTraversal(self):
        res = []
        stack = []
        prev = None
        root = self.root

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()

            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node
                # root = None
            else:
                stack.append(node)
                root = node.right

        return res
    
    def levelorderTraversal(self):
        root = self.root
        if not root:
            return []
        
        queue = [root]
        res = []

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if level:
                res.append(level)
        
        return res

    def buildFromPreIn(self, preorder, inorder):
        def createtree(preorder, inorder, n):
            if n == 0: return None
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            node = TreeNode(inorder[k])
            node.left = createtree(preorder[1 : k + 1], inorder[0 : k], k)
            node.right = createtree(preorder[k + 1:], inorder[k:], n - k - 1)
            return node
        createtree(preorder, inorder, len(inorder))
    
    def buildFromInPost(self, inorder, postorder):
        def createtree(inorder, postorder, n):
            if n == 0: return None
            k = 0
            while postorder[-1] != inorder[k]:
                k += 1
            node = TreeNode(inorder[k])
            node.left = createtree(inorder[:k], postorder[:k], k)
            node.right = createtree(inorder[k + 1 :], postorder[k : n - 1], n - k - 1)
            return node
        createtree(inorder, postorder, len(inorder))

tree = Tree()
values = [5, 3, 7, 2, 4, 6, 8]
for v in values:
    tree.insert(v)

print(tree.preorderTraversal2())
print(tree.inorderTraversal())
print(tree.postorderTraversal())