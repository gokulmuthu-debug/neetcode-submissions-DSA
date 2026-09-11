class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        if len(nums)==0: return 0
        n=len(nums)
        res=0
        prev1=nums[0]
        prev2=max(nums[0], nums[1])
        res=max(prev1, prev2)
        for i in range(2, n):
            res=max(prev2, prev1+nums[i])
            prev1=prev2
            prev2=res
        return res