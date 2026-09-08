class Solution:
    def bfs(self, r: int, c: int, grid: List[List[str]], visit: set, rows: int, cols: int):
        q=collections.deque()
        visit.add((r, c))
        q.append((r, c))
        while q:
            row, col = q.popleft()
            dirs=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in dirs:
                r=row+dr
                c=col+dc
                if r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        visit=set()
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r, c) not in visit:
                    self.bfs(r, c, grid, visit, rows, cols)
                    islands+=1
        return islands