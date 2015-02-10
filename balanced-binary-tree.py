# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        depth, balance = self.isBalancedRec(root)
        return balance

    def isBalancedRec(self, root):
        if root is None:
            return 0, True
        depth = 1
        depthL, balanceL = self.isBalancedRec(root.left)
        depthR, balanceR = self.isBalancedRec(root.right)
        depth += max(depthL, depthR)
        balance = balanceL and balanceR and \
            (depthL == depthR or depthL == depthR + 1 or depthL + 1 == depthR)
        return depth, balance
