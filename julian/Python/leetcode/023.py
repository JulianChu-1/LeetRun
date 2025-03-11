import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
ListNode.__lt__ = lambda a, b : a.val < b.val
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()

        h = [head for head in lists if head]
        heapq.heapify(h)

        while h:
            node = heapq.heappop(h)

            if node.next:
                heapq.heappush(h, node.next)
            cur.next = node
            cur = cur.next
            
        return dummy.next
