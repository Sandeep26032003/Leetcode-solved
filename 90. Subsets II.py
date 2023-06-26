class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        buffer = []
        res_list = [[]]

        elements = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                elements += [nums[i]]
            else:
                elements = [nums[i]]
                res_list += buffer
                buffer = [] 
            buffer += [ l + elements for l in res_list]
        return res_list + buffer
        
