# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for i in lists:
            while i:
                lst.append(i.val)
                i = i.next
        lst = sorted(lst)
        a = ListNode(0)
        temp = a
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
