class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        lo,hi=0,len(nums)-1
        mod = 10**9+7
        count=0
        while lo<=hi:
            if nums[lo]+nums[hi]<=target:
                count+=pow(2,hi-lo)
                lo+=1
            else:
                hi-=1
        return count%mod

            
