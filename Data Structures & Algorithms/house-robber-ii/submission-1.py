class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums[0], nums[1])
        n=len(nums)
        arr1=(n-1)*[0]
        arr2=(n-1)*[0]
        for i in range(0, n-1):
            arr1[i]=nums[i]
        for i in range(1, n):
            arr2[i-1]=nums[i]
        prev1=arr1[0]
        prev2=max(arr1[0], arr1[1])
        res1=max(prev1, prev2)
        for i in range(2, n-1):
            res1=max(prev2, prev1+arr1[i])
            prev1=prev2
            prev2=res1
        prev1=arr2[0]
        prev2=max(arr2[0], arr2[1])
        res2=max(prev1, prev2)
        for i in range(2, n-1):
            res2=max(prev2, prev1+arr2[i])
            prev1=prev2
            prev2=res2
        return max(res1, res2)