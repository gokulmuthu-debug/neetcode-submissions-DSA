class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total=0
        l=0
        minlen=len(nums)+1
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                minlen=min(r-l+1, minlen)
                total-=nums[l]
                l+=1
        if minlen==len(nums)+1: return 0
        return minlen
