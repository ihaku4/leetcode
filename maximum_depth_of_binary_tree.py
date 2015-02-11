# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [(root, 1)]
        maxDepth = 0
        while len(stack) > 0:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return maxDepth

from binary_tree_builder import BinaryTree
from binary_tree_printer import BinaryTreePrinter

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.bt = BinaryTree()
        self.bp = BinaryTreePrinter()
        self.bp.printStructureLine = False
        serials = ['{1,2,2,3,3,3,3,4,4,4,4,4,4,#,#,5,5} ',
                   '{1111111111111,2,2,3,3333333,3,3,4,44444444444,44,4444,4,4,#,#,5,5} ',
                   '{1, #, 2, #, 3}', 
                   ]
        self.cases = {}
        for serial in serials:
            root = self.bt.deserialize(serial)
            # self.bp.printTree(root)
            treeGraph = self.bp.drawTreeGraphByString(root)
            self.cases[root] = treeGraph.count('\n')
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        for c in self.cases:
            graph = self.bp.drawTreeGraphByString(c)
            print graph
            print graph.encode('hex')
            print len(graph)
            print self.bp._lineWidth
            self.assertEqual(self.cases[c], self.s.maxDepth(c))

if __name__ == '__main__':
    unittest.main()
    # bt = BinaryTree()
    # bp = BinaryTreePrinter()
    # bp.printStructureLine = False
    # # serials = ['{1,2,2,3,3,3,3,4,4,4,4,4,4,#,#,5,5} ',
    # #            '{1111111111111,2,2,3,3333333,3,3,4,44444444444,44,4444,4,4,#,#,5,5} ',
    # #            '{1, #, 2, #, 3}', ]
    # serial = '{1,2,2,3,3,3,3,4,4,4,4,4,4,#,#,5,5} '
    # root = bt.deserialize(serial)
    # bp.printTree(root)
    # bp.printTree(root)
    # treeGraph = bp.drawTreeGraphByString(root)
    # print treeGraph.count('\n')
