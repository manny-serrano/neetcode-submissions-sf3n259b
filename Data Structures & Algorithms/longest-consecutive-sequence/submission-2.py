class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        found = set(nums)

        maxlen = 0 
        for number in nums:
            if (number-1) not in found:
                length=1
                while (number+length) in found:
                    length+=1
                maxlen = max(length, maxlen)
        return maxlen
            