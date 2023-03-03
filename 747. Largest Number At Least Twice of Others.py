class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        if nums1[len(nums1)-1]>= 2*nums1[len(nums1)-2]:
            for i in range(len(nums)):
                if nums[i] == nums1[len(nums1)-1]:
                    return i
                    break
        else:
            return -1
