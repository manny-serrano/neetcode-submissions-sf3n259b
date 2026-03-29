class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input is array nums, 
        
        
        n = len(nums)

        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in reversed(range(n)):
            result[i] *= suffix
            suffix *= nums[i]

        return result






            
            

                







       

            
            


        