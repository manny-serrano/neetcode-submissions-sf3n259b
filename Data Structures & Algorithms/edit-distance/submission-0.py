class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # inout is 2 strings, output is int
        # 2d dynamic programming

        # initiate 2d array
        cache = [[float('inf')]*(len(word2)+1) for i in range(len(word1)+1)]
        # fill bottom row of grid

        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2) - j 

        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1)-i
        

        #base case of 2d array

        # bottom up so work backwards

        for i in range(len(word1)-1, -1, -1 ): # decrementing order until 0th index
            for j in range(len(word2)-1, -1, -1):
                # 2 cases either chars equal or not equal
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else: # check all 3 directions
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])

        return cache[0][0] # tells us min number for beginning of both strings, entire






