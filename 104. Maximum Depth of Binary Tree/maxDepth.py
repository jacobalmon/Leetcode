# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0

        leftD = self.maxDepth(root.left)
        rightD = self.maxDepth(root.right)

        if leftD < rightD:
            return 1 + rightD
        
        return 1 + leftD
        
