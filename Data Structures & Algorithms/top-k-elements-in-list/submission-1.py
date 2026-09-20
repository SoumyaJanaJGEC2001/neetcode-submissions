class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        p = counts.most_common(k)
        return [i[0] for i in p]