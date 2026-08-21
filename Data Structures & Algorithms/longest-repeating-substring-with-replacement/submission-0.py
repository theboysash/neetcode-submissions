class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        best = 0
        max_freq = 0
        l = 0 
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0)+1
            max_freq = max(max_freq, count[s[r]])
            if (r-l+1)-max_freq>k:
                count[s[l]] = count.get(s[l])-1
                l+=1
            best = max(best, r-l+1) 
        return best