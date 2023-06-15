class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        nums.sort()

        for i,val in enumerate(nums):
            if i>0 and val == nums[i-1]:
                continue
            lo,hi = i+1,len(nums)-1
            while lo<hi:
                s = val+nums[lo]+nums[hi]
                if s>0: hi-=1
                elif s<0: lo+=1
                else:
                    lst.append([val,nums[lo],nums[hi]])
                    lo+=1
                    while nums[lo] == nums[lo-1] and lo<hi:
                        lo+=1
        return lst
