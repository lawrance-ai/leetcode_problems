class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = "qwertyuiop"
        b = "asdfghjkl"
        c = "zxcvbnm"
        op = []
        for i in words:
            y = i.lower()
            y = set(y)
            if y.issubset(a):                
                op.append(i)
            elif y.issubset(b):
                op.append(i)
            elif y.issubset(c):
                op.append(i)
        return op
