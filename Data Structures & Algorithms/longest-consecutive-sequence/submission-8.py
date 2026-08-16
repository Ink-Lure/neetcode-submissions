class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortNums = sorted(list(set(nums)))
        index, res = 0, {0: []}
        for i, x in enumerate(sortNums):
            if sortNums[i] - sortNums[i-1] <= 1:
                res[index].append(x)
            else:
                index += 1
                res[index] = [x]
        return len(sorted([x for i,x in res.items()], key=len, reverse=True)[0])

        