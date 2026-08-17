class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        n=len(s2)
        if k>n: return False
        l=0
        map1={}
        map2={}
        for i in range(k):
            map1[s1[i]]=1+map1.get(s1[i], 0)
            map2[s2[i]]=1+map2.get(s2[i], 0)
        if map1==map2: return True
        for r in range(k,n):
            map2[s2[r]]=1+map2.get(s2[r], 0)
            map2[s2[l]]-=1
            if map2[s2[l]]==0: map2.pop(s2[l])
            l+=1
            if map1==map2: return True
        return False