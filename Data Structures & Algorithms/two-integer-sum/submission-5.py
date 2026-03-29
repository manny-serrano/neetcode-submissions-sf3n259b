class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # smallest index first
        # get index and value at the same time
        found = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in found:
                return [found[diff], i]
            else:
                found[num] = i


        