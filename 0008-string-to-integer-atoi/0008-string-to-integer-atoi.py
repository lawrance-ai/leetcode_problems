class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        op = ''
        flag = 0
        if s == "":
            return 0
        if s[0] == '-':
            flag = 1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for i in s:
            if i in '9876543210':
                op += i
            else:
                break
        op = int(op) if op else 0
        if flag == 1:
            op *= -1
        if op > 2**31 - 1:
            return 2**31 - 1
        elif op < -2**31:
            return -2**31
        return op