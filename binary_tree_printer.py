class BinaryTreePrinter(object):
    def __init__(self, printStructureLine=False):
        self._nodesOfCurrentLine = []
        self._printedWidth = 0
        self._spaces = []
        self._lineWidth = 0
        self._line0 = ''
        self._line1 = ''
        self._line2 = ''
        self._line3 = ''
        self.printStructureLine = printStructureLine
        pass

    def printNodeStructureLine(self, node):
        vWidth = self.intWidth(node.val)
        i = len(self._line2)
        while i < len(self._spaces) and self._spaces[i]:
            self._line2 += ' '
            self._line3 += ' '
            i += 1

        #              3333333
        #                 |
        #          ---------------
        #         44            4444
        #
        # <------><><-><-----><><--><----->
        # 1       2 3  4      5 6   7
        #
        # 1. llWidth
        # 2. lvWidth
        # 3. lrWidth
        # 4. vWidth
        # 5. rl..
        # 6. rv..
        # 7. rr..
        if node.left:
            llWidth = self.nodeWidth(node.left.left)
            lrWidth = self.nodeWidth(node.left.right)
            lvWidth = self.intWidth(node.left.val)
            # self._line2 += ' ' * (llWidth + lvWidth / 2)
            # self._line2 += '-' * (lvWidth - lvWidth/2 + lrWidth + vWidth/2)
            self._line2 += ' ' * (llWidth + lvWidth / 2)
            self._line2 += ' '
            self._line2 += '-' * (lvWidth - lvWidth/2 + lrWidth + vWidth/2 - 1)

            self._line3 += ' ' * (llWidth + lvWidth / 2)
            self._line3 += '/'
            self._line3 += ' ' * (lvWidth - lvWidth/2 + lrWidth + vWidth/2 - 1)
        if node.right:
            rlWidth = self.nodeWidth(node.right.left)
            rrWidth = self.nodeWidth(node.right.right)
            rvWidth = self.intWidth(node.right.val)
            # self._line2 += '-' * (vWidth - vWidth/2 + rvWidth - rvWidth/2 + rlWidth)
            # self._line2 += ' ' * (rvWidth/2 + rrWidth)
            self._line2 += '-' * (vWidth - vWidth/2 + rvWidth - rvWidth/2 + rlWidth - 1)
            self._line2 += ' '
            self._line2 += ' ' * (rvWidth/2 + rrWidth)

            self._line3 += ' ' * (vWidth - vWidth/2 + rvWidth - rvWidth/2 + rlWidth - 1)
            self._line3 += '\\'
            self._line3 += ' ' * (rvWidth/2 + rrWidth)

    def printNode(self, node):
        lWidth = self.nodeWidth(node.left)
        rWidth = self.nodeWidth(node.right)
        vWidth = self.intWidth(node.val)
        while self.positionOcuppied():
            self.printString(' ')
        nodePos = self._printedWidth + lWidth

        if self.printStructureLine:
            self.printNodeStructureLine(node)

        self.markNode(nodePos, vWidth)

        self.printString(' ' * lWidth)
        self.printString(str(node.val),
                         self.printStructureLine and (node.left or node.right))
        self.printString(' ' * rWidth)

    def printString(self, s, isNode=False):
        # sys.stdout.write(s)
        self._line0 += s
        if isNode:
            l = [' '] * len(s)
            l[len(s) / 2] = '|'
            self._line1 += ''.join(l)
        else:
            self._line1 += ' ' * len(s)
        self._printedWidth += len(s)
        if self._printedWidth == self._lineWidth:
            # sys.stdout.write('\n')
            self._line0 += '\n'
            self._line1 += '\n'
            self._line2 += '\n'
            self._line3 += '\n'
            if self.printStructureLine:
                self._line0 += self._line1
                self._line0 += self._line2
                self._line0 += self._line3
            self._line1 = ''
            self._line2 = ''
            self._line3 = ''
            self._printedWidth = 0
            # self.drawLines()

    def drawLines(self):
        #   1       2
        #   |       |       : line1
        # -----   -----     : line2
        # |   |   |   |     : line3
        line1 = ''
        # line2 = ''
        # line3 = ''
        while len(self._nodesOfCurrentLine) > 0:
            node = self._nodesOfCurrentLine.pop(0)
            i = 0
            while self.positionOcuppied():
                self._line2 += ' '
                self._line3 += ' '
                i += 1

            # XXX Spaces on the Left !!!
            line1 += ' ' * (self.nodeWidth(node.left) + len(str(node.val)) / 2)
            line1 += '|'

    def markNode(self, start, length):
        i = start
        while i < start + length:
            self._spaces[i] = True
            i += 1

    def positionOcuppied(self):
        return self._spaces[self._printedWidth]

    def printTree(self, root):
        print self.drawTreeGraphByString(root)
        print

    def drawTreeGraphByString(self, root):
        self.__init__(self.printStructureLine)
        queue = [root]
        self._lineWidth = self.nodeWidth(root)
        self._spaces = [False] * self._lineWidth
        while len(queue) > 0:
            node = queue.pop(0)
            self._nodesOfCurrentLine.append(node)
            self.printNode(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if self._line0[-1] != '\n':
            self._line0 += ' ' * (self._lineWidth - self._printedWidth) + '\n'
        return self._line0

    def nodeWidth(self, root):
        if root is None:
            return 0
        lwidth = self.nodeWidth(root.left)
        rwidth = self.nodeWidth(root.right)
        return lwidth + rwidth + self.intWidth(root.val)

    def intWidth(self, num):
        return len(str(num))


import unittest
# from binary_tree_builder import BinaryTree


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
