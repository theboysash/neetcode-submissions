class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = ''.join(c.lower() for c in s if c.isalnum())
        if not s:
            isPalindrome = True
        s2 = s[::-1]
        isPalindrome = True
        for i in range(len(s)):
            if s[i] == s2[i]:
                isPalindrome = True
            else: 
                isPalindrome = False
                break
            
        
        return isPalindrome
        