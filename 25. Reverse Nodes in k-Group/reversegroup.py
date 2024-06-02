# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode()
        dummy.next = head
        prevG = dummy
        curr = head
        
        while True:
            kth = self.getKth(prevG, k)
            if not kth:
                break
            nextG = kth.next

            prev = kth.next
            curr = prevG.next

            while curr != nextG:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prevG.next
            prevG.next = kth
            prevG = temp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
