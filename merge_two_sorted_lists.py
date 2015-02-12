# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1 
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        mergeNode = head
        while l1 and l2:
            if l1.val < l2.val:
                mergeNode.next = l1
                mergeNode = l1
                l1 = l1.next
            else:
                mergeNode.next = l2
                mergeNode = l2
                l2 = l2.next
        mergeNode.next = l1 if l1 else l2
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
        mList = self.s.mergeTwoLists(list1, list2)
        self.printLinkedList(mList)

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
