class Solution
{
public:
    int maxProfit(vector<int>& prices)
    {
        if(prices.size()<=1) return 0;
        int left, right, max_profit;
        max_profit=0;
        left=0; right=1;
        while(left<prices.size() && right<prices.size())
        {
            max_profit=max(max_profit, (prices[right]-prices[left]));
            if(prices[right]-prices[left]<0) left=right;
            right++;
        }
        return max_profit;
    }
};
