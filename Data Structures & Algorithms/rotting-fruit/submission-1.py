from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS - counter for each iteration
        #Visited Rotten 
        #Queue of rotten to go through

        visited = set()
        queue = deque()

        rows, cols = len(grid), len(grid[0])
        fresh_count = 0

        #Find rotten fruit - Add to visited - Add to Queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh_count +=1
        #Weve just found all the rotten apples and the number of fresh apples

        #Counter will track the total time taken
        counter = 0

        if fresh_count == 0:
            return 0

        #we now need to find the fresh apples make them rotten and add them to queue

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(1,0), (-1, 0), (0,-1), (0,1)]:
                    nr, nc = r+dr, c+dc 

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        fresh_count -=1
                        if fresh_count == 0:
                            return counter+1
            counter += 1 
        return -1