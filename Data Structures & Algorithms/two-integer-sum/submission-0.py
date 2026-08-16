class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in have: return [have[diff], i]
            have[nums[i]]=i
        return []