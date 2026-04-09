class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        found = defaultdict(list)


        for i in strs:
            charfreq = [0]*26
            for chara in i: 
                charfreq[ord(chara)-ord('a')] += 1
            found[tuple(charfreq)].append(i)

        for key, value in found.items():
            result.append(list(value))
        return result
        
            
        