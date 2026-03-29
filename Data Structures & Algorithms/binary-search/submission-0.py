class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) -1

        while l<r:
            middle = l+((r-l)//2)

            if nums[middle] >= target:
                r = middle
            elif nums[middle] < target:
                l=middle +1
                
            
        return l if (l<len(nums) and nums[l] == target)else -1
        