class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_lst = list(s)
        ans=""
        for i in order:
            while i in s_lst:
                ans+=i
                s_lst.remove(i)
        return ans+"".join(s_lst)
        
