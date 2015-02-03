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
        setB = set([headB])
        while headA.next is not None or headB.next is not None:
            if headA.next is not None:
                setA.add(headA.next)
                headA = headA.next
            if headB.next is not None:
                setB.add(headB.next)
                headB = headB.next
            inter = setA.intersection(setB)  # XXX
            if len(inter) != 0:
                return inter.pop()
        return None
