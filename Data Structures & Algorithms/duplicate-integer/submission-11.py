class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #duplicate use hashmap/hashset

        return len(set(nums)) != len(nums)
        