# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthOfBinaryTree(self, root) -> int:
        if root is None:
            return 0 
        return 1 + max(self.depthOfBinaryTree(root.left), self.depthOfBinaryTree(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        diameterAtRoot = self.depthOfBinaryTree(root.left) + self.depthOfBinaryTree(root.right)
        return max(diameterAtRoot, self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)) 