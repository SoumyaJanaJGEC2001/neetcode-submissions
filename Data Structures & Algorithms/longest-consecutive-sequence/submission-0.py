class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if (num - 1) not in s:
                num = num + 1
                length = 1
                while num in s:
                    num += 1
                    length += 1
                longest = max(longest,length)
        return longest