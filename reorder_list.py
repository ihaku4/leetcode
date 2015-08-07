# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        length = self.lengthOfList(head)
        if length < 2:
            return

        nodeStack = []
        node = head
        for i in xrange(length / 2):
            nodeStack.append(node)
            node = node.next

        nodeInTheMiddle = nodeStack[-1]
        if length % 2 == 1:
            nodeInTheMiddle = node
            node = node.next
        nodeInTheMiddle.next = None

        while nodeStack:
            tailNodeInList1 = nodeStack.pop()
            currentNodeForInsertion = node
            node = node.next
            currentNodeForInsertion.next = tailNodeInList1.next
            tailNodeInList1.next = currentNodeForInsertion
        return

    def lengthOfList(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def printList(self, node):
        while node:
            print '%d -> ' % node.val,
            node = node.next
        print



import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        self.head.next = node2
        node2.next = node3
        node3.next = node4 
        pass

    def test_default_case(self):
        h = Solution().reorderList(self.head)
        self.printList(h)

    def printList(self, node):
        while node:
            print '%d -> ' % node.val,
            node = node.next
        print

if __name__ == '__main__':
    unittest.main()
