class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        op = []
        n = len(nums)
        nums_set = set(nums)
        for i in range(1, n + 1):
            if i not in nums_set:
                op.append(i)
        return op