class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        p = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        n = len(digits)
        if n == 0:
            return []
        res = ['']
        for i in range(n):
            res = [s + c for s in res for c in p[int(digits[i]) - 2]]
        return res