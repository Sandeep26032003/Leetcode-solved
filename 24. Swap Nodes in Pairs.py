# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i in range(0,len(lst)-1,2):
            lst[i],lst[i+1]=lst[i+1],lst[i]
        a = ListNode(0)
        temp = a
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next

        
