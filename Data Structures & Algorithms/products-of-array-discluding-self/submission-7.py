class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        for x in nums:
            if x == 0:
                zeros += 1
            else:
                prod *= x

        if zeros > 1:
            return [x * 0 for x in nums]

        newList = []
        for x in nums:
            if zeros == 1 and x != 0:
                newList.append(0)
            elif zeros == 1 and x == 0:
                newList.append(prod)
            elif zeros == 0:
                newList.append(int(prod / x))
        
        return newList

        