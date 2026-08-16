class Solution
{
public:
    int characterReplacement(string s, int k)
    {
        int hash[256]={0};
        int res=0;
        int l=0;
        int maxf=0;
        for(int r=0; r<s.length(); r++)
        {
            hash[s[r]]++;
            maxf=max(maxf, hash[s[r]]);
            while((r-l+1)-maxf>k)
            {
                hash[s[l]]--;
                l++;
            }
            res=max(res, r-l+1);
        }   
        return res;
    }
};
