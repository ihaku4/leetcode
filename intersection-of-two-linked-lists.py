# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        setA = set([headA])
        while headA.next is not None:
            setA.add(headA.next)
            headA = headA.next
        while headB is not None:
            if headB in setA:
                return headB
            headB = headB.next
        return None
