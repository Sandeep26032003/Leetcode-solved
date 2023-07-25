class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = " ".join(s).split()
        goal = " ".join(goal).split()
        for _ in range(len(s)):
            if s == goal:
                return True
            else:
                s.insert(0,s.pop())
        return False
        
        
