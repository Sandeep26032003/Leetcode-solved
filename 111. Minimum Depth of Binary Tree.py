# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root, depth):
            if not root:
                return float('inf')
            elif not root.left and not root.right:
                return depth
            l = dfs(root.left, depth + 1)
            r = dfs(root.right, depth + 1)
            return min(l, r)
        return dfs(root, 1)
