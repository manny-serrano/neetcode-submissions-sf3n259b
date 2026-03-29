class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        found = {}

        for i,num in enumerate(nums):
            difference = target - num

            if difference in found:
                return [found[difference], i]
            
            else:
                found[num] = i 
        
        
        