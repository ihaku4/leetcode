# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        target = head
        i = head
        while n > 0:
            i = i.next
            n -= 1
        if i is None:
            return head.next
        while i.next is not None:
            i = i.next
            target = target.next
        target.next = target.next.next
        return head
