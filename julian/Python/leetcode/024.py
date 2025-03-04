from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy

        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next

            cur.next = node2
            node1.next = node2.next
            node2.next = node1
            cur = node1
            
        return dummy.next