# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        level = [root]
        result = []
        while len(level) > 0:
            result.append([n.val for n in level])
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
                level = newLevel
        return result

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
            print self.s.levelOrder(c)
            # self.assertEqual(self.cases[c], self.s{})}

if __name__ == '__main__':
    unittest.main()
