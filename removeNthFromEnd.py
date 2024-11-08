#remove-nth-node-from-end-of-list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printNodes(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0,head)
        first = last = res
        for _ in range(n):
            if first.next:
                first = first.next
        while first.next:
            first = first.next
            last = last.next
        last.next = last.next.next
        return res.next
        
"""
if __name__ == "__main__":
    solution = Solution()
    four = ListNode(4)
    three = ListNode(3, four)
    two = ListNode(2, tres)
    one = ListNode(1, two)
    solution.removeNthFromEnd(one, 2)
    solution.printNodes(one)
"""
