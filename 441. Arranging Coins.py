class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0;i=1
        while n>0:
            count+=i
            i+=1
            n-=i
        print(n,i)
        if n<0:return i-1
        return i-1
