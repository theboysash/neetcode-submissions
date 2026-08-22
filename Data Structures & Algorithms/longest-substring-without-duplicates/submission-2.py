class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we need to keep track of max
        #we need to slide right 
        #if character in seen we remove that character and go to the next 
        seen = set()
        l = 0
        count = 0
        best = 0
        for r in range(0, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
                count-=1
            seen.add(s[r])
            best = max(best, r-l+1)
        return best
    
            
           
                

                
       