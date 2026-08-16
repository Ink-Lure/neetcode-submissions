class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        for x in nums:
            if x != 0:
                prod *= x
            else:
                zeros += 1

        match(zeros):
            case 0:
                return [int(prod / x) for x in nums]
            case 1:
                return [prod if x == 0 else 0 for x in nums]
            case _:
                return [x * 0 for x in nums]

        