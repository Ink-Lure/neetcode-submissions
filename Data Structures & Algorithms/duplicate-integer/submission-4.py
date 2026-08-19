class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] > 1 if len(nums) > 1 else False
        