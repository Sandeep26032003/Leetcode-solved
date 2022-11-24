class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    n={}
    for i in nums:
      if i in n:
        n[i]+=1
      else:
        n[i]=1
    for i,j in n.items():
      if j==1:
return i
