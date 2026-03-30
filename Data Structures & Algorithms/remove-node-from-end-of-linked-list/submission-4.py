# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = dummy = ListNode(0, head)
        r = head

        # move right pointer n times to the right
        while n:
            r = r.next
            n -= 1
        
        # move two pointers simontaniously to the right
        while r:
            r = r.next
            l = l.next

        # delete the next node of the left pointer
        l.next = l.next.next

        # return the first node after the dummy
        return dummy.next