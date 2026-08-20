class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #keep track of best, after 1 recursion we get area return max area 

        rows, cols = len(grid), len(grid[0])
        visited = set()
        area = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >=cols or (r,c) in visited or grid[r][c] ==0:
                return 0
            visited.add((r,c))
            area=1
            for dr, dc in [(1,0),(-1,0), (0,1),(0,-1)]:
                area += dfs(r+dr,c+dc)
            return area
        best = 0       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    best = max(best, dfs(r,c))
        return best
        