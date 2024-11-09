# merge-k-sorted-lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            current.next = l1 if l1 else l2
            return dummy.next
            
        merged_list = lists[0]
        for i in range(1, len(lists)):
            merged_list = mergeTwoLists(merged_list, lists[i])
        return merged_list
