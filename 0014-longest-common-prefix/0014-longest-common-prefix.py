class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        p = ""
        c = 0
        if len(strs) == 1:
            p += strs[0]
            return p
        for c in range(len(strs[0])):
            for i in range(len(strs) - 1):
                if c >= len(strs[i+1]) or strs[0][c] != strs[i+1][c]:
                    return p
            p += strs[0][c]
        return p