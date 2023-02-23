# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i in range(len(lst)):
            if i == left-1:
                lst[i:right] = lst[i:right][::-1]
        a = ListNode(0)
        temp = a
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
