# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)
        lst=[]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    lst.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        return sorted(lst)[k-1]
