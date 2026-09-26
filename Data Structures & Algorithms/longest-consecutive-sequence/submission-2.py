class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        for n in nums:
            if (n-1) not in s:
                next_n = n+1
                length = 1
                while next_n in s:
                    length += 1
                    next_n += 1
                l = max(l,length)
        return l