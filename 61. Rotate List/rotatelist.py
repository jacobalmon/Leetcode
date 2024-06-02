# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head

        dummy = ListNode()
        dummy.next = head
        curr = head
        length = 1

        while curr.next:
            curr = curr.next
            length += 1

        k = k % length
        if k == 0:
            return dummy.next

        curr2 = head
        for i in range(length - k - 1):
            curr2 = curr2.next

        dummy.next = curr2.next
        curr2.next = None
        curr.next = head

        return dummy.next
        
