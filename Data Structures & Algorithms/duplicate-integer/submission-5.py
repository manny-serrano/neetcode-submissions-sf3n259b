class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list2 = set(nums)
        if len(list2) < len(nums):
            return True
        else:
            return False

        