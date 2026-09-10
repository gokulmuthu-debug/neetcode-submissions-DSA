class Solution:
    def dfs(self, course: int, seen: set(), premap: {}, res: List[int]):
        if course in seen: return False
        if premap[course] is None: return True
        seen.add(course)
        for b in premap[course]:
            if not self.dfs(b, seen, premap, res): return False
        res.append(course)
        seen.remove(course)
        premap[course]=None
        return True
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap={i:[] for i in range(numCourses)}
        seen=set()
        for a, b in prerequisites:
            premap[a].append(b)
        res=[]
        for b in range(numCourses):
            if not self.dfs(b, seen, premap, res): return []
        return res