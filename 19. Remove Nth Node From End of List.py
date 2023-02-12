# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst = lst[::-1]
        for i in range(0,len(lst)):
            if i == n-1:
                del lst[i]
        a = ListNode(0)
        temp = a
        for i in lst[::-1]:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
