class Solution:
    def countBits(self, n: int) -> List[int]:
        x1=[]
        for i in range(n+1):
            x = bin(i).replace("ob","")
            x = x.count("1")
            x1.append(x)
        return x1
