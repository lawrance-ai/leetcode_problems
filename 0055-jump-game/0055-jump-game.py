class Solution:
    def canJump(self, nums: list[int]) -> bool:
        st = []
        n = len(nums)
        i = 0
        if nums[0]==0 and n==1:
            return True
        if nums[0]==0:
            return False
        while i<n:
            st.append(nums[i])
            i+=1
        x = st.pop(0)
        j = x
        while j>0:
            if len(st)==0:
                return True
            a = st.pop(0)
            if a>=j:
                j = a
                continue
            j-=1
            
        if len(st)==0:
            return True
        return False