class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r = max(candies)
        ncl = []
        for i in range(len(candies)):
            candies[i]+=extraCandies
            if candies[i]>=r:
                ncl.append(True)
            else:
                ncl.append(False)
        return ncl
        
