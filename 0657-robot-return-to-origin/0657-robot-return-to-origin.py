class Solution:
    def judgeCircle(self, moves: str) -> bool:
        stack = []
        n = 4
        dict = {"U":"D","D":"U","R":"L","L":"R"}
        for i in moves:
            if stack and stack[-1] == dict[i]:
                stack.pop()
            else:
                stack.append(i)
        if stack:
            n = len(stack)-1
            while n > 0:
                m = stack[n]
                if dict[m] in stack:
                    stack.remove(dict[m])
                    stack.pop()
                    n-=2
                else:
                    break
        return not stack