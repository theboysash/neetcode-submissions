class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        left = 0
        best = 0
        for right in range(len(s)):
            current = s[right]
            if current in tracker:
                left = max(left, tracker[current]+1)
            tracker[current] =  right
            total = right - left + 1
            if total > best:
                best = total
        return best
