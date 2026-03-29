class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # we want to return the indexes of the numbers within the nums array that when added can sum to the target

    # since every input satisfies the condition, we can just take the target and subtract by the i and look for another one that equals

    
        map1 = {}
        for i, value in enumerate(nums):
            difference = target - value
            if difference in map1: 
                return sorted([map1[difference], i])
            map1[value] = i

        





