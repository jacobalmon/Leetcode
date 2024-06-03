# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        leftD = ListNode()
        rightD = ListNode()
        currL = leftD
        currR = rightD

        while head:
            if head.val < x:
                currL.next = head
                currL = currL.next
            else:
                currR.next = head
                currR = currR.next

            head = head.next

        currL.next = rightD.next
        currR.next = None
        return leftD.next
        
