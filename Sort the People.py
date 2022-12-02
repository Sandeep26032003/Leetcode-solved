class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x1=[]
        x=zip(heights,names)
        for i,j in sorted((x),reverse=True):
            x1.append(j)
        return x1
        
