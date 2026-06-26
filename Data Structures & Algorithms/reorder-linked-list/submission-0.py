# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        total = []

        start = head
        while start:
            total.append(start)
            start = start.next
        
        
        l = 0
        r = len(total) - 1

        while l < r:
            total[l].next = total[r]
            l += 1
            if l < r:
                total[r].next = total[l]
            r -= 1
        if l == r:
            total[r].next = None
        else:
            total[l].next = None

