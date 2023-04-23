class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3:
            return max(nums)
        else:
            nums = list(set(nums))
            nums.sort(reverse=True)
            return nums[2]
