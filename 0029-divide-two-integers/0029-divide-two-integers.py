class Solution:
    def divide(self, dividend: int, divisor: int) -> int:        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        q = dividend
        d = divisor
        if q<-2**31:
            return -2**31
        elif q>2**31-1:
            return 2**31-1
        neg = False
        if q<0 and d>0:
            q *=-1
            neg = True
        elif d<0 and q>0:
            d *= -1
            neg = True
        elif q<0 and d<0:
            q *=-1
            d*=-1
        
        ans = q//d
        if neg:
            ans*=-1
        return max(ans,INT_MIN)