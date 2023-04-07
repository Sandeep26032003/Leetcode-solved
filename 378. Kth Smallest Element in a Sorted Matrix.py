class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst=[]
        for i in matrix:
            lst+=i
        return sorted(lst)[k-1]
