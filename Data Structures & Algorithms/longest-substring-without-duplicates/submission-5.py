class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we have to keep track of th echars visited
        #we have to keep appending a char we havent seen
        #if we see a char in our visited set, we remove   the     value of the left pointer

        visited = set()
        l = 0
        best = 0
        for r in range(0, len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1
            visited.add(s[r])
            best = max(best, r-l+1)
            
        return best
            
            



   