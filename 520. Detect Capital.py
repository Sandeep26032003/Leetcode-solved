class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        elif word.isupper():
            return True
        else:
            for i in range(len(word)):
                if word[i].isupper() and word[i+1:].islower():
                    return True
                return False
            
