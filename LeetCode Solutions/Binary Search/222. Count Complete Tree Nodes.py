# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # Helper function to compute the height of the tree.
        def compute_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        if not root:
            return 0
        
        left_height = compute_height(root.left)
        right_height = compute_height(root.right)
        
        if left_height == right_height:
            # Left subtree is perfect, so we count all nodes in left + root and recurse on the right
            return (2 ** left_height) + self.countNodes(root.right)
        else:
            # Right subtree is perfect, so we count all nodes in right + root and recurse on the left
            return (2 ** right_height) + self.countNodes(root.left)
            