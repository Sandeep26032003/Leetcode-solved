# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lst=[]
        lowlst=[]
        highlst=[]
        x_index = 0
        while head:
            lst.append(head.val)
            head = head.next
        for i in range(len(lst)):
            if lst[i]<x:
                lowlst.append(lst[i])
            else:
                highlst.append(lst[i])
        a = ListNode(0)
        temp = a
        for i in lowlst+highlst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
