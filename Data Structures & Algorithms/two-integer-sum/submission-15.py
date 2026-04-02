class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        found = {}

        for i, value in enumerate(nums):
            difference = target - value
            if difference in found:
                return [found[difference], i]
            found[value] = i 
        
       