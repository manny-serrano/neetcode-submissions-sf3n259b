class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for word in strs:
            wordsort = sorted(word)
            sorted_word = "".join(wordsort)
            if sorted_word in found:
                found[sorted_word].append(word)
            else:
                found[sorted_word] = [word]

        output = []
        for x in found:
            output.append(found[x])
        return output

            

            


        