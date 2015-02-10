# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None:
            return []
        stack = [root]
        level = []
        valueList = []
        while len(stack) > 0:
            level = stack
            stack = []
            levelValue = []
            for n in level:
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
                levelValue.append(n.val)
            valueList.insert(0, levelValue)
        return valueList

from binary_tree_builder import BinaryTree
from binary_tree_printer import BinaryTreePrinter

bt = BinaryTree()
# root = bt.deserialize('{1,2,3,#,#,4,#,#,5}')
root = bt.deserialize('{3,9,20,#,#,15,7}')
btp = BinaryTreePrinter()
print btp.drawTreeGraphByString(root)
s = Solution()
print s.levelOrderBottom(root)
print s.levelOrderBottom(None)
