class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, number in enumerate(nums):
            difference = target - number
            if difference in found:
                return [found[difference], i]
            else:
                found[number] = i 



        