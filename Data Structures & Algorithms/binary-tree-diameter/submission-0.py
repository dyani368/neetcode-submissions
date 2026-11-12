# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 

        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            return 1+max(left,right)
        
        left = depth(root.left)
        right = depth(root.right)

        self.res = max(self.res,left+right)

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        
        return self.res


        