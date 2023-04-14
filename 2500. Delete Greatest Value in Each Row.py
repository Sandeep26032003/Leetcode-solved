class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i = i.sort(reverse = True)
        sum=0
        for i in zip(*grid):
            print(i)
            sum+=max(i)
        return sum
