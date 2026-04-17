class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers)-1

        while l<r:
            targetsum = numbers[l] + numbers[r]
            if targetsum == target:
                return [l+1, r+1]
            elif targetsum < target:
                l+=1
            else:
                r-=1
        
                
        