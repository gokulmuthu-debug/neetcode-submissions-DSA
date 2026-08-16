class Solution
{
public:
    string minWindow(string s, string t)
    {
        int hash[256]={0};
        int l=0; int r=0;
        int minLen=INT_MAX; int sidx=-1;
        int cnt=0;
        int n=s.length(); int m=t.length();
        for(int i=0; i<m; i++) hash[t[i]]++;
        while(r<n)
        {
            if(hash[s[r]]>0) cnt++;
            hash[s[r]]--;
            while(cnt==m)
            {
                if(r-l+1<minLen)
                {
                    minLen=r-l+1;
                    sidx=l;
                }
                hash[s[l]]++;
                if(hash[s[l]]>0) cnt--;
                l++;
            }
            r++;
        }
        if(sidx==-1) return "";
        string res="";
        for(int i=sidx; i<sidx+minLen; i++) res+=s[i];
        return res;
    }
};
