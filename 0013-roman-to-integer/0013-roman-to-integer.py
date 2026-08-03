class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        t = 0
        n = len(s)
        s += '\0'
        for i in range(n):
            j = s[i]
            if s[i] == 'I'  and s[i+1] !='\0' and (s[i+1] =='X'or s[i+1] =='V'):
                t -= 1
                continue
            elif s[i] == 'X' and s[i+1] !='\0' and (s[i+1] =='L' or s[i+1] =='C'):
                t -= 10
                continue
            elif s[i] == 'C' and s[i+1] !='\0' and (s[i+1] =='M' or  s[i+1] =='D'):
                t -= 100
                continue
            t += dict[j]
        return t


        