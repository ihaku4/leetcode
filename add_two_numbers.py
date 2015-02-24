# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return None
        head, carry = self.addTwoNode(l1, l2)
        ln = head
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            ln.next, carry = self.addTwoNode(l1, l2, carry)
            ln = ln.next
        while l1.next:
            l1 = l1.next
            ln.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) / 10
            ln = ln.next
        while l2.next:
            l2 = l2.next
            ln.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) / 10
            ln = ln.next
        if carry:
            ln.next = ListNode(1)
        return head

    def addTwoNode(self, n1, n2, carry=0):
        value = (n1.val + n2.val + carry) % 10
        carry = (n1.val + n2.val + carry) / 10
        return ListNode(value), carry


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        pass

    def printList(self, node):
        if not node:
            return ''
        string = ''
        while node:
            string += str(node.val) + ' -> '
            node = node.next
        return string[:-4]

    def buildList(self, string):
        pass

    def test_default_case(self):
        self.assertEqual(True, True)
        self.assertTrue(True)
        # self.assertEqual(, self.s.)
        self.printList()

if __name__ == '__main__':
    unittest.main()
