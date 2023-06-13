# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        lc=1
        d={}
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:q.append(node.left)
                    if node.right:q.append(node.right)
            if sum(level) not in d: d[sum(level)] = lc
            lc+=1
        return d[max(d)]
