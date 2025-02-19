from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # 迭代(双指针)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre
    
    # 递归
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur, pre):
            if not cur:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res

        return recur(head, None)