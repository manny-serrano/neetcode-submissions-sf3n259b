class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for ind, value in enumerate(nums):
            difference = target - value

            if difference in found:
                return [found[difference], ind]
            found[value] = ind




        