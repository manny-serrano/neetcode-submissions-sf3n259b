class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        found = set(nums)
        maxlen = 0 

        for num in nums:
            if (num-1) not in found:
                
                length =1
                while (num + length) in found:
                    length+=1
                maxlen = max(length, maxlen)
        return maxlen

                





        
        
