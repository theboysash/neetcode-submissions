class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r>= rows or c>= cols or board[r][c] !=word[i] or (r,c) in visited):
                return False
            visited.add((r,c))
            found = False
            for dr, dc in [(1,0), (-1, 0), (0,-1), (0,1)]:
                if dfs(r+dr, c+dc, i+1):
                    found = True
                    break
            visited.remove((r,c))
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, 0):
                    return True
        return False

