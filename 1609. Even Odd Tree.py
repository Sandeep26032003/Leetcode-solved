# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        lc = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(level) != len(set(level)): return False
            if level and lc%2 == 1:
                if level == sorted(level)[::-1]:
                    for i in range(len(level)):
                        if level[i]%2 == 0:
                            continue
                        else:
                            return False
                else: return False
            else:
                if level == sorted(level):
                    for i in range(len(level)):
                        if level[i]%2 == 1:
                            continue
                        else:
                            return False
                else: return False
            lc+=1
        return True
