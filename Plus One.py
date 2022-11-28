class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = int(''.join(map(str,digits)))
        str1 = str1+1
        return list(str(str1))
    
