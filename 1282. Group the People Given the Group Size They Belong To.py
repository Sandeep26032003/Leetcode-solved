class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d.keys():
                d[groupSizes[i]]=[i]
            elif groupSizes[i] in d.keys():
                d[groupSizes[i]]+=[i]
        lst=[]
        for i,j in d.items():
            if i != len(j):
                for k in range(0,len(j),i):
                    lst.append(j[k:k+i])
            else:
                lst.append(j)
        return lst
