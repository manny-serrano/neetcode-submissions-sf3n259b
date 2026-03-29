class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        keymap1 = defaultdict(list)
        
        for word in strs:
            charfreq = [0]*26
            for j in word:
                charfreq[ord(j) - ord('a')] += 1
            keymap1[tuple(charfreq)].append(word)

        return list(keymap1.values())
            



        