class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0 
        l = 0 
        visited = set()
        for r in range(0, len(s)):
            
            while s[r] in visited:
                visited.remove(s[l])
                l+=1 
            visited.add(s[r])
            length = r - l + 1
            best = max(best, length)
        return best
            

        