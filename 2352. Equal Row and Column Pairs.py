class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        lst=[]
        for i in zip(*grid):
            lst.append(list(i))
        for i in range(len(lst)):
            for j in grid:
                if lst[i]==j:
                    count+=1
                else:
                    count+=0
        return count
