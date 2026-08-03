class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x<0:
            x = x*-1
            flag = 1
        op = int(str(x)[::-1])
        if flag == 1:
            op = op*-1
        if op<-2**31 or op>2**31-1:
            return 0
        return op
