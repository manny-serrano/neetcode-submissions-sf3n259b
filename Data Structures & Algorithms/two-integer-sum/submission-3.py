class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keeps track of key values, with num being key, i being value (index)
        diction = {}
        #enumerate is index,value 
        for i,num in enumerate(nums):
            difference = (target - num)
            #difference is possible value num can be paired with to reach target
            # if the difference is already found, we return that key value, which is the index, and the current i
            if difference in diction:
                return [diction[difference], i]
            diction[num] = i
                
            

            

            



        