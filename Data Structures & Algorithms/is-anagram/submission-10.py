class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input is strings, output is boolean
        

        return sorted(s) == sorted(t)


        