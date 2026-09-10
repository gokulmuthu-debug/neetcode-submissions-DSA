class Solution:
    def bfs(self, r: int, c: int, grid: List[List[str]], rows: int, cols: int, seen: set()):
        q=collections.deque()
        seen.add((r, c))
        q.append((r, c))
        while q:
            row, col = q.popleft()
            dirs=[[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dirs:
                r=row+dr
                c=col+dc
                if (r in range(rows) and
                c in range(cols) and grid[r][c]=="1" and (r, c) not in seen):
                    seen.add((r, c))
                    q.append((r, c))
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands=0
        seen=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r, c) not in seen:
                    self.bfs(r, c, grid, rows, cols, seen)
                    islands+=1
        return islands