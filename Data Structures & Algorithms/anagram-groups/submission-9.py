class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        keymap2 = defaultdict(list)
        for word in strs:
            freqmap = [0]*26
            for i in word:
                freqmap[ord(i) - ord('a')] += 1
            keymap2[tuple(freqmap)].append(word)
        return list(keymap2.values())
                

        
        