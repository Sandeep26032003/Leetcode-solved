class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1 = sorted(list(set(nums)))
        if nums1==sorted(nums):
            return False
        else:
            return True
