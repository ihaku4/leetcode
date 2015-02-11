# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)

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
        self.caseList = []
        for serial in serials:
            root = self.bt.deserialize(serial)
            # self.bp.printTree(root)
            treeGraph = self.bp.drawTreeGraphByString(root)
            self.cases[root] = treeGraph.count('\n')
            self.caseList.append(root)
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        for c in self.cases:
            graph = self.bp.drawTreeGraphByString(c)
            print graph
            # print graph.encode('hex')
            # print len(graph)
            # print self.bp._lineWidth
            print self.s.isSameTree(c, c)
            # self.assertEqual(self.cases[c], self.s{})}
        print self.s.isSameTree(self.caseList[0], self.caseList[1])
        t1 = self.bt.deserialize('{10,5,15}')
        t2 = self.bt.deserialize('{10,5,#,#,15}')
        self.bp.printTree(t1)
        self.bp.printTree(t2)
        print self.s.isSameTree(t1, t2)

if __name__ == '__main__':
    unittest.main()
