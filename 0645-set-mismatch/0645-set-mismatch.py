class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        op = []
        a =0
        b=0
        for i in range(1,n+1):
            if nums.count(i)>1:
                a = i
            if i not in nums:
                b = i
            if a!=0 and b!=0:
                break
        op.append(a)
        op.append(b)
        return op
