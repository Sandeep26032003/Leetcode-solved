class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l_lst = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                l_lst.append(nums[i])
        for i in range(len(nums)):
            if nums[i]==pivot:
                l_lst.append(nums[i])
        for i in range(len(nums)):
            if nums[i]>pivot:
                l_lst.append(nums[i])
        return l_lst
