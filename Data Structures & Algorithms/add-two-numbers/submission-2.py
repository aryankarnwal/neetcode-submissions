# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            new = ListNode()
            if carry:
                total = l1_val + l2_val + + 1
            else:
                total = l1_val + l2_val

            
            carry = total//10
            val = total % 10

            new.val = val

            head.next = new
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            head.next = ListNode(val=1)

        return dummy.next