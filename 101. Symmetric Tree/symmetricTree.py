# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        return self.mirrored(root.left, root.right)

    def mirrored(self, left, right):
        if not left and not right:
            return True

        if  not left or not right:
            return False

        return (
            left.val == right.val and 
            self.mirrored(left.left, right.right) and 
            self.mirrored(left.right, right.left)
        )
        
