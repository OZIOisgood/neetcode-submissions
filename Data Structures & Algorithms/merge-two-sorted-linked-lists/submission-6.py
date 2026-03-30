# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1; r = list2

        if not l: return r
        if not r: return l

        dummy = prev = ListNode()

        while l and r:
            if l.val < r.val:
                prev.next = l
                prev = l
                l = l.next
            else:
                prev.next = r
                prev = r
                r = r.next
        prev.next = l or r
        return dummy.next