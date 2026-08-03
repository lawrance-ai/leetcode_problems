class Solution:
    def isValid(self, s: str) -> bool:
        op = []
        o = ["[","{","("]
        c = ["]","}",")"]
        s = list(s)
        def ind(l,x):
            for i in range (len(l)):
                if l[i] == x:
                    return i            
        while (s):
            a = s.pop()
            if  a in c:
                op.append(a)
            else:
                if a in o and len(op)==0:
                    return False
                elif a in o and ind(o,a) != ind(c,op[-1]):
                    return False
                op.pop()                    
        if op:
            return False
        else:
            return True