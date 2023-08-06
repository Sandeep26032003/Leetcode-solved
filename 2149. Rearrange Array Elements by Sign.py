class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pl = []
        nl = []
        for i in range(len(nums)):
            if nums[i]>0:pl.append(nums[i])
            else: nl.append(nums[i])
        ans=[]
        for i in range(len(pl)):
            ans.append(pl[i])
            ans.append(nl[i])
        nums[:] = ans[:]
        return nums
