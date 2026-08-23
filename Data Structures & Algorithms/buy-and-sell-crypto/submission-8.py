class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res=0
        s=0
        for r in range(len(prices)):
            s=prices[r]-prices[l]
            res=max(res, s)
            if s<0: l=r
        return res