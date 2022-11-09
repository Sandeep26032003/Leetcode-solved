class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st = ""
        for i in range(len(s)):
            for j in range(len(indices)):
                if i == indices[j]:
                    st += s[j]
        return st
