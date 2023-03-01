class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        primes = [2,3,5,7,11,13,16,17,19]
        for i in range(left,right+1):
            if ((bin(i)[2:]).count("1")) in primes:
                count+=1
        return count
        
