class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m = len(nums)
        i = 0
        j = n
        ans = []
        while(i<n and j<m):
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j+=1
        return ans