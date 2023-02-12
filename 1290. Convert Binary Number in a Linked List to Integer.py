# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head:
            l.append(str(head.val))
            head = head.next
        s = ""
        return int(s.join(l),2)
