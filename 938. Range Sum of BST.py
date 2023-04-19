# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        range_of_bst = [i for i in range(low,high+1)]
        range_sum=0
        while stack:
            node = stack.pop()
            if node.val in range_of_bst:
                range_sum+=node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return range_sum
