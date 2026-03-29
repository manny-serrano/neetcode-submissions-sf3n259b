class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keymap = defaultdict(list)

        for word in strs:
            charfreq = [0]*26
            for j in word:
                charfreq[ord(j)-ord('a')] +=1
            keymap[tuple(charfreq)].append(word)
        return list(keymap.values())
            
                
                
        
        