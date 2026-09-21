class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_mult = r_mult = 1
        l = [0]*n
        r = [0]*n
        for i in range(n):
            j = -i-1
            l[i] = l_mult
            r[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        return [l*r for l,r in zip(l,r)]