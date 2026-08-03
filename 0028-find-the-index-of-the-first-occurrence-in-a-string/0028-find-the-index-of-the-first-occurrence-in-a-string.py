class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        a = haystack
        b = needle
        y = b[0]
        if len(haystack)<len(needle):
            return -1
        def ind(z):
            o = []
            for i in range(len(haystack)):
                if haystack[i]==z:
                    o.append(i)
            return o
        n = ind(needle[0])
        
        for i in n:
            op =""                 
            start_index = i
            if a[start_index] != y:
                return -1
            if start_index>=len(haystack):
                continue
            l = 0
            m = start_index
            while l<len(needle):
                if m>=len(haystack):
                    break
                if needle[l] != haystack[m]:
                    break
                op+=needle[l]
                m+=1
                l+=1
            if op == needle:
                ans = start_index
                return ans
        return ans   