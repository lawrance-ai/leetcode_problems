class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = -1
        if target in nums:
            return nums.index(target)
        j = len(nums)-1
        while(j>=0):
            if nums[j]<target:
                return j+1
            j-=1
        return j+1            