class Solution:
    def dfs(self, course: int, seen: set(), premap: {}):
        if course in seen: return False
        if premap[course]==[]: return True
        seen.add(course)
        for b in premap[course]:
            if not self.dfs(b, seen, premap): return False
        seen.remove(course)
        premap[course]=[]
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        seen=set()
        for a, b in prerequisites:
            premap[a].append(b)
        for i in range(numCourses):
            if not self.dfs(i, seen, premap): return False
        return True