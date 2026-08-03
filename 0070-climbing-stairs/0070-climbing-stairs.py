class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=2
        c=0
        if n==2:
            return b
        if n==1:
            return a
        for i in range(2,n):
           c=a+b
           a=b
           b=c
        return c 