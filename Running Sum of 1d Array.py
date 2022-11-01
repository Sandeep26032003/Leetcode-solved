class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        fnums = []
        sum = 0
        for i in range(len(nums)):
            sum = sum+nums[i]
            fnums.append(sum)
        return fnums
            
