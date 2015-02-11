# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        delNode = None
        node = head
        if not head:
            return head
        while node.next:
            if delNode:
                if node.val != node.next.val:
                    delNode.next = node.next
                    delNode = None
            elif node.val == node.next.val:
                delNode = node
            node = node.next
        if delNode:
            delNode.next = None
        return head


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        list1 = self.buildLinkedList('1->1->2')
        list2 = self.buildLinkedList('1->1->2->3->3')
        self.printLinkedList(list1)
        self.printLinkedList(list2)

        ulist1 = self.s.deleteDuplicates(list1)
        ulist2 = self.s.deleteDuplicates(list2)
        self.printLinkedList(list1)
        self.printLinkedList(list2)
        self.printLinkedList(ulist1)
        self.printLinkedList(ulist2)

    def buildLinkedList(self, s):
        s = s.strip()
        values = s.split('->')
        root = ListNode(values[0])
        node = root
        for v in values[1:]:
            node.next = ListNode(v)
            node = node.next
        return root

    def printLinkedList(self, node):
        out = ''
        while node:
            out += node.val + ' -> '
            node = node.next
        print out

if __name__ == '__main__':
    unittest.main()
