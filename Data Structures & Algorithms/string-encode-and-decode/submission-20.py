class Solution:

    def encode(self, strs: List[str]) -> str:

        # need to turn list of strings into one huge string,need to distinguish something
        #for start/end of word

        encoded = ""
        for i in strs:
            # Prepend length and a delimiter to handle cases where "#" is in the string
            encoded += str(len(i)) + "#" + i
        return encoded

    def decode(self, s: str) -> List[str]:

        output = []
        ind = 0
        while ind < len(s):
            # Find the delimiter to get the length
            j = ind
            while s[j] != "#":
                j += 1
            length = int(s[ind:j])
            # Extract the string based on the parsed length
            output.append(s[j+1 : j+1+length])
            # Move the pointer to the start of the next encoded block
            ind = j + 1 + length

        return output