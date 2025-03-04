from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        flag = 0
        
        while l1 or l2 or flag:
            if l1:
                flag += l1.val
                l1 = l1.next
            if l2:
                flag += l2.val
                l2 = l2.next
            cur.next = ListNode(flag % 10)
            flag //= 10
            cur = cur.next
        
        return dummy.next

