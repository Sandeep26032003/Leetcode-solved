# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        sum=0
        while head:
            if head.val == 0:
                if sum:
                    lst.append(sum)
                sum=0
            else:
                sum+=head.val
            head = head.next
        a = ListNode(0)
        temp = a
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next

                

                
