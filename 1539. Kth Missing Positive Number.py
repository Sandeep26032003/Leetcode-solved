class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lst=[]
        for i in range(len(arr)+k+1):
            if i not in arr:
               lst.append(i)
        return lst[k]
