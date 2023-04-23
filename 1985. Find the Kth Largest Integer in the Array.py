class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        lst = [int(i) for i in nums]
        lst.sort(reverse=True)
        return str(lst[k-1])
        
