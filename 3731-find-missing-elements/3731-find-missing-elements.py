class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        op = []
        nums.sort()
        max = nums[-1]
        min = nums[0]
        for i in range(min+1,max):
            if i not in nums:
                op.append(i)
        return op