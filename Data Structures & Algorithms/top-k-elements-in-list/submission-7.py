class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(iter:=Counter(nums), key=iter.get, reverse=True)[:k]
        