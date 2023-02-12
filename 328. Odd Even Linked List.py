# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        odd_lst = []
        even_lst = []
        for i in range(len(lst)):
            if i%2 != 0:
                odd_lst.append(lst[i])
            else:
                even_lst.append(lst[i])
        final_lst = even_lst+odd_lst
        a = ListNode(0)
        temp = a
        for i in final_lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
