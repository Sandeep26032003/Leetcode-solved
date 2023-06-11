class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = []
        max_length = 0
        char = 0
        while char<len(s):
            if s[char] not in visited:
                visited.append(s[char])
                max_length = max(max_length,len(visited))
                char+=1
            else:
                visited.pop(0)
        return max_length
