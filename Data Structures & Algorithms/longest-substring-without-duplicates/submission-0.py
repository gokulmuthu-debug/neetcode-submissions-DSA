class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CharSet= set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in CharSet:
                CharSet.remove(s[l])
                l+=1
            CharSet.add(s[r])
            res=max(res, r-l+1)
        return res