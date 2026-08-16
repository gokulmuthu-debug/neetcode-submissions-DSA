class Solution 
{
public:
    int lengthOfLongestSubstring(string s) 
    {
        int l=0; int res=0;
        set<char> charSet;
        for(int r=0; r<s.length(); r++)
        {
            while(1)
            {
                auto it=charSet.find(s[r]);
                if(it!=charSet.end())
                {
                    charSet.erase(s[l]);
                    l++;
                }
                else break;
            }
            charSet.insert(s[r]);
            res=max(res, r-l+1);
        } 
        return res;
    }
};
