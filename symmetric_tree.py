# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def _isSymmetric(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left and root.right or \
           not root.right and root.left:
            return False
        lstack = [root.left]
        rstack = [root.right]
        while len(lstack) > 0 or len(rstack) > 0:
            if len(lstack) != len(rstack):
                return False
            l = lstack.pop()
            r = rstack.pop()
            if l.val != r.val or \
               not l.left and r.right or \
               l.left and not r.right or \
               not l.right and r.left or \
               l.right and not r.left:
                return False
            if l.left and r.right:
                lstack.append(l.left)
                rstack.append(r.right)
            if l.right and r.left:
                lstack.append(l.right)
                rstack.append(r.left)
        return True

    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetricRec(root.left, root.right)

    def isSymmetricRec(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.isSymmetricRec(left.left, right.right) and \
               self.isSymmetricRec(left.right, right.left)


from binary_tree_builder import BinaryTree
from binary_tree_printer import BinaryTreePrinter

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.bt = BinaryTree()
        self.bp = BinaryTreePrinter()
        self.bp.printStructureLine = True
        serials = ['{1,2,2,3,3,3,3,4,4,4,4,4,4,#,#,5,5} ',
                   '{1111111111111,2,2,3,3333333,3,3,4,44444444444,44,4444,4,4,#,#,5,5} ',
                   '{1, #, 2, #, 3}',
                   '{1, 2, 2, 3, 4, 4, 3}',
                   '{1, 2, 2, #, 3, #, 3}',
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
            # print graph.encode('hex')
            # print len(graph)
            # print self.bp._lineWidth
            print self.s.isSymmetric(c)
            # self.assertEqual(self.cases[c], self.s{})}

if __name__ == '__main__':
    unittest.main()
