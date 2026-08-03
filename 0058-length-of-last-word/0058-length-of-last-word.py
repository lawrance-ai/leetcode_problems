class Solution:
    def lengthOfLastWord(self, s: str) -> int:        
        s=s.strip()
        if len(s)==1:
            return 1
        s=list(s)
        i = s[-1]
        c = 0
        d = len(s)-1
        while(i!=' 'and d>=0):
            c+=1
            d-=1
            i=s[d]
        return c