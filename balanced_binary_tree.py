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

from binary_tree_builder import BinaryTree
# from binaray_tree_builder import TreeNode
from binary_tree_printer import BinaryTreePrinter

# tree = BinaryTree('{1, #, 2, #, 3}')
# tree = BinaryTree('{1,#,2,#,3}')
serial = '{1,2,2,3,3,3,3,4,4,4,4,4,4,#,#,5,5} '
serial = '{1111111111111,2,2,3,3333333,3,3,4,44444444444,44,4444,4,4,#,#,5,5} '
serial = '{1, #, 2, #, 3}'
tree = BinaryTree(serial)
root = tree.deserialize()
print Solution().isBalanced(root)
printer = BinaryTreePrinter()
printer.printStructureLine = False
printer.printStructureLine = True
printer.printTree(root)
print serial
