# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def length_of_list(head):
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    return length

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        length = length_of_list(head)

        if length == 0:
            return True
        if length == 1:
            return True
        if length == 2:
            return head.val == head.next.val
        if length == 3:
            return head.val == head.next.next.val
        
        # reverse head half
        half_length = length / 2

        if half_length >= 2:
            # O ->  O ->        O ->
            # head  head_next   nxt
            head_next = head.next
            nxt = head.next.next

            head.next = None
            head_next.next = head
            # <- O  <- O        O ->
            # head  head_next   nxt

            head = head_next
            # <- O  <- O        O ->
            #       head_next   nxt
            #       head

            half_length -= 1
            
            while half_length >= 2:
                head_next = nxt
                nxt = nxt.next
                # <- O  O ->        O ->
                # head  head_next   nxt

                head_next.next = head
                head = head_next
                # <- O  <- O        O ->
                #       head_next   nxt
                #       head
                half_length -= 1

        # compare head and tail
        head_middle_2 = nxt
        head_middle_1 = head

        if length % 2 != 0:
            nxt = nxt.next

        while head and nxt and head.val == nxt.val:
            head = head.next
            nxt = nxt.next

        is_palindrome = head is None

        # restore head
        while head_middle_1 is not None:
            nxt_1 = head_middle_1.next
            # <- O      <- O            O ->
            # nxt_1     head_middle_1   head_middle_2
            head_middle_1.next = head_middle_2
            head_middle_2 = head_middle_1
            head_middle_1 = nxt_1
            # <- O          O ->            O ->
            # head_middle_1 head_middle_2

        return is_palindrome
