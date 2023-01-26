class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        lst=[]
        for i in words:
            row_cnt1=0
            row_cnt2=0
            row_cnt3=0
            s = i.lower()
            for j in s:
                if j in row1:
                    row_cnt1+=1
                elif j in row2:
                    row_cnt2+=1
                else:
                    row_cnt3+=1
            if row_cnt1==len(i) or row_cnt2==len(i) or row_cnt3==len(i):
                lst.append(i)
        return lst
