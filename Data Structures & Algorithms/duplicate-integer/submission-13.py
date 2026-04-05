class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #input is int array, output is boolean

        return len(set(nums)) != len(nums)


        