class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        op = 0
        i = 0
        a = 0
        while(i<len(nums)):
            if nums[i]==1:                
                a += 1
            else:
                op = max(op,a)
                a = 0
            i+=1
        op = max(op,a)
        return op