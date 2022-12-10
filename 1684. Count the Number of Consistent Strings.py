class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            count1=0
            for j in i:
                if j not in allowed:
                    count1+=1
            if count1==0:
                count+=1
            count1=0
        return count
