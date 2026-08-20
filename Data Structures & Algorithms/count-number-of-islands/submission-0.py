class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #setup 
        # rows columns set
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r<0 or r >= rows or c<0 or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return
            visited.add((r,c))
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r+dr, c+dc)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    count+=1
        

        return count

        