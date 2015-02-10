import sys


class BinaryTreePrinter(object):
    def __init__(self):
        pass

    def printString(self, s, printedWidth, lineWidth):
        sys.stdout.write(s)
        printedWidth += len(s)
        if printedWidth == lineWidth:
            sys.stdout.write('\n')
            printedWidth = 0
        return printedWidth

    def printTree(self, root):
        queue = [root]
        lineWidth = self.nodeWidth(root)
        spaces = [False] * lineWidth
        printedWidth = 0
        while len(queue) > 0:
            node = queue.pop(0)
            lWidth = self.nodeWidth(node.left)
            rWidth = self.nodeWidth(node.right)
            vWidth = self.intWidth(node.val)
            # XXX print pad
            # XXX print no newline !!!
            while spaces[printedWidth]:
                printedWidth = self.printString(' ', printedWidth, lineWidth)
            # for i in range(lWidth, lWidth + vWidth):
            for i in range(printedWidth + lWidth, printedWidth + lWidth + vWidth):
                spaces[i] = True
            printedWidth = self.printString(' ' * lWidth, printedWidth, lineWidth)
            # XXX node.val -> len !!
            printedWidth = self.printString(str(node.val), printedWidth, lineWidth)
            printedWidth = self.printString(' ' * rWidth, printedWidth, lineWidth)

            # XXX add new node, add current to spaces
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # new line
            # left blank
        print

    def nodeWidth(self, root):
        if root is None:
            return 0
        lwidth = self.nodeWidth(root.left)
        rwidth = self.nodeWidth(root.right)
        return lwidth + rwidth + self.intWidth(root.val)

    def intWidth(self, num):
        return len(str(num))


import unittest
from binaray_tree_builder import BinaryTree


class Test(unittest.TestCase):
    def setUp(self):
        self.t = BinaryTreePrinter()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        self.assertEqual(self.t.intWidth(100), 3)
        self.assertEqual(self.t.intWidth(1100), 4)
        self.assertEqual(self.t.intWidth(-1100), 5)
        self.assertEqual(self.t.intWidth(-1), 2)
        self.assertEqual(self.t.intWidth(1), 1)
        self.assertEqual(self.t.intWidth(0), 1)

if __name__ == '__main__':
    unittest.main()
