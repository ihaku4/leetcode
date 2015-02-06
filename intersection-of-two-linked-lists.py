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

        countA = countB = 0
        headACp = headA
        while headACp is not None:
            countA += 1
            headACp = headACp.next
        headBCp = headB
        while headBCp is not None:
            countB += 1
            headBCp = headBCp.next

        headACp = headA
        headBCp = headB
        if countA > countB:
            for i in range(countA - countB):
                headACp = headACp.next
        elif countB > countA:
            for i in range(countB - countA):
                headBCp = headBCp.next

        while headACp != headBCp and headACp is not None:
            headACp = headACp.next
            headBCp = headBCp.next

        return headACp
