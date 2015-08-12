# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        length = self.lengthOfList(head)
        return self.sortListHelper(head, length)

    def sortListHelper(self, head, length):

        # Tackle minimal situation.
        if length == 0:
            return head
        if length == 1:
            head.next = None
            return head

        # Split current list into 2 sublists recursively,
        # Break in the middle.
        secondHead = head
        for i in xrange(length / 2):
            secondHead = secondHead.next

        # Sort the two sublists separately.
        head = self.sortListHelper(head, length / 2)
        secondHead = self.sortListHelper(secondHead, length - length / 2)

        # Merge the two sorted sublists.
        newHead = self.mergeList(head, secondHead)
        return newHead

    # TODO this method is Slow! Find out why.
    def mergeList(self, firstHead, secondHead):
        cur = ListNode(0)
        newHead = cur
        while firstHead and secondHead:
            if firstHead.val <= secondHead.val:
                cur.next = firstHead
                cur = firstHead
                firstHead = firstHead.next
            else:
                cur.next = secondHead
                cur = secondHead
                secondHead = secondHead.next
        while firstHead:
            cur.next = firstHead
            cur = firstHead
            firstHead = firstHead.next
        while secondHead:
            cur.next = secondHead
            cur = secondHead
            secondHead = secondHead.next

        # Break the last node link.
        cur.next = None

        return newHead.next

    def lengthOfList(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

def printList(node):
    while node:
        print '%d -> ' % node.val,
        node = node.next
    print

def main():
    head = ListNode(3)
    node2 = ListNode(1)
    node3 = ListNode(5)
    node4 = ListNode(2)
    node5 = ListNode(7)

    head.next = node2
    #node2.next = node3
    #node3.next = node4
    #node4.next = node5

    h = Solution().sortList(head)
    printList(h)


if __name__ == '__main__':
    main()
