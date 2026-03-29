class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        found = defaultdict(list)


        for s in strs:
            mappedchar = [0]*26
            for element in s:
                mappedchar[ord(element) - ord('a')] += 1
            found[tuple(mappedchar)].append(s)
        return list(found.values())
        