class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # WE keep track of a left and right pointer 
        #we keep track of a max area 
        #we move left if right is bigger
        #we move right if left is bigger

        l = 0
        r = len(heights) - 1
        best = 0
        while l < r:
            width = r-l
            height = min(heights[r], heights[l])
            area = width * height 
            best = max(area, best)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return best
