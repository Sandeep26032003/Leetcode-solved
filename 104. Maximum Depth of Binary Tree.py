# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        max_depth = 0
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
            max_depth+=1
        return max_depth-1