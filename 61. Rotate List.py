# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        else:
            lst = []
            while head:
                lst.append(head.val)
                head = head.next 
            for _ in range(k%len(lst)):
                lst.insert(0,lst.pop())
            a = ListNode(0)
            temp = a
            for i in lst:
                temp.next = ListNode(i)
                temp = temp.next
            return a.next
            
