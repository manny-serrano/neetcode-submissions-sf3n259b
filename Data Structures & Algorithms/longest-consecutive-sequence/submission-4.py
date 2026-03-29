class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest = 0 

        for n in numset:
            if (n-1) not in numset:
                lengthseq = 0
                while (n+lengthseq) in numset:
                    lengthseq+=1
                longest = max(lengthseq, longest)
        return longest
        