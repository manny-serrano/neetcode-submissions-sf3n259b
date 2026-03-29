class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key, value in count.items():
            freq[value].append(key)

        output = []
        for c in range(len(freq)-1, 0, -1):
            
            for element in freq[c]:
                output.append(element)
                if len(output) == k:
                    return output