class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(0, len(heights)):
            for j in range(0, len(heights)):
                if i == j:
                    continue
                x_distance=j-i
                y_distance= min(heights[i], heights[j])
                area = x_distance * y_distance
                if area > maximum:
                    maximum = area
        return maximum
                
                
        