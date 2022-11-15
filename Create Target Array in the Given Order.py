class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_arr = []
        for i,j in zip(nums,index): 
            target_arr[j:j] = [i]
            print(target_arr)
        return target_arr
