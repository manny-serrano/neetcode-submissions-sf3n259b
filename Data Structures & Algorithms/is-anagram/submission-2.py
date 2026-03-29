class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we want to check 2 strings and see if they have the same characters, its does not matter the order
        # 2 arguments, return a boolean
        #edge cases, they are not the same length
        #have to exaclty the same characters
        #can youse a hasmap to put keys and their values then check if they are equal


        map1, map2 = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            # put char in that string into the map and add one for each time that character is in it
            map1[s[i]] = map1.get(s[i], 0) + 1
            map2[t[i]] = map2.get(t[i], 0) + 1
            # if they are anagarams this should be True
        return map1 == map2



        
                 