# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = ""
        lst2 = ""
        while l1 :
            lst1+=str(l1.val)
            l1 = l1.next
        while l2:
            lst2+=str(l2.val)
            l2 = l2.next
        lst3 = " ".join(str(int(lst1[::-1])+int(lst2[::-1]))).split()[::-1]
        a = ListNode(0)
        temp = a
        for i in lst3:
            temp.next = ListNode(int(i))
            temp = temp.next
        return a.next
        
