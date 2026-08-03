class Solution:
    def concatenatedBinary(self, n: int) -> int:
        op = ""
        m = 1000000007
        for i in range (1,n+1):
            op += bin(i)[2:]
        return (int(op,2)%m)