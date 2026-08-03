class Solution:
    def minOperations(self, s: str) -> int:
            s = list(s)
            count1 = 0
            count2 = 0
            for i in range (len(s)):
                if i%2==0 and s[i] != '1':
                     count1 += 1
                elif i%2 != 0 and s[i] != '0':
                     count1 += 1
                if i%2==0 and s[i] != '0':
                     count2 += 1
                elif i%2 != 0 and s[i] != '1':
                     count2 += 1                     
            if count1 < count2:
                 ans = count1
            else:
                 ans = count2
            return ans