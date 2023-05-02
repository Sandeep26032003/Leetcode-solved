class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if digits == "": # blank case
            return []
        chars=[]
        for c in digits:
            chars.append(dict[c])
        code = product(*chars)
        #The product() function from the itertools module generates the cartesian product of the input iterables.
        lst = []
        for k in code:
            lst.append(''.join(k))
        return lst
