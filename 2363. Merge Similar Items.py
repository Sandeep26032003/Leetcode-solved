class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        f_lst=[]
        d = {}
        for v1,w1 in items1:
            if v1 not in d:
                d[v1] = w1
        for v2,w2 in items2:
            if v2 in d:
                d[v2]+=w2
            else:
                d[v2] = w2
        for i,j in d.items():
            f_lst.append([i,j])
        f_lst.sort()
        return f_lst
