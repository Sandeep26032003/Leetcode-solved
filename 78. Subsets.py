class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        for i in range(len(nums)+1):
            lst+=list(combinations(nums,i))
        return lst
        
