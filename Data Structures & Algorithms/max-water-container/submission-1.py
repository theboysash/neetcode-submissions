class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # keep track od distance r-1
        # take min height of 
        l = 0
        r = len(heights)-1
        maxArea = 0
        while r != l:
            area = min(heights[l], heights[r]) * (r-l)
            maxArea = max(area, maxArea)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return maxArea