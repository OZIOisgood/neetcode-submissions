# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # Save next
            nxt = curr.next

            # Reverse
            curr.next = prev
            
            # Shift pointers
            prev = curr
            curr = nxt
        
        return prev