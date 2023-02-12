# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        lst2 = []
        while list1:
            lst1.append(list1.val)
            list1 = list1.next
        while list2:
            lst2.append(list2.val)
            list2 = list2.next
        final_lst = sorted(lst1+lst2)
        a = ListNode(0)
        temp = a
        for i in final_lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
        
