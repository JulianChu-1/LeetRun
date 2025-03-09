from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(node):
            cur, pre = node, None
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next
        
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        
        left_node = pre.next
        curr = right_node.next

        pre.next = None
        right_node.next = None

        reverse(left_node)

        pre.next = right_node
        left_node.next = curr

        return dummy.next



