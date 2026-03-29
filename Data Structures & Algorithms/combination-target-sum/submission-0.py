class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
       


        result = []

        def backtrack(startInd, remaining, currentCombination):
            #base case already hit target
            if remaining == 0:
                result.append(currentCombination[:]) # appends copy of current Combination into result
                return 
            elif remaining <0:
                return 

            for i in range(startInd, len(nums)):
                currentCombination.append(nums[i])
                backtrack(i, remaining - nums[i], currentCombination)
                currentCombination.pop()



        backtrack(0, target, [])
        return result



        