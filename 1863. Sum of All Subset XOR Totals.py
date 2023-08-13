class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        subsets = []
        def dfs(i):
            if i>=len(nums):
                res = subsets.copy()
                if len(res)>0:
                    xor_result = reduce(lambda x,y:x^y,res)
                    ans.append(xor_result)
                else:
                    ans.append(0)
                return 
            subsets.append(nums[i])
            dfs(i+1)
            subsets.pop()
            dfs(i+1)
        dfs(0)
        return sum(ans)
    
