class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortNums, index, res = sorted(list(set(nums))), 0, {0: []}
        for i, x in enumerate(sortNums):
            if sortNums[i] - sortNums[i-1] <= 1:
                res[index].append(x)
            else:
                res[index+1], index = [x], index + 1
        return len(sorted([x for i,x in res.items()], key=len, reverse=True)[0])

        