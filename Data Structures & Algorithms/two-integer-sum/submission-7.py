class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in list:
                return [list[x],i]
            list[nums[i]]=i