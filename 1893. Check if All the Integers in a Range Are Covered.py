class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        inclusive_range = []
        for i in range(left,right+1):
            inclusive_range.append(i)
        for i in ranges:
            for j in range(i[0],i[1]+1):
                if j in inclusive_range:
                    inclusive_range.remove(j)
        return len(inclusive_range)==0
