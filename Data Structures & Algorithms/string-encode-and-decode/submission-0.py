class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = str()
        for string in strs:
            length = len(string)
            new_string += str(length) + "#" + string
        return new_string

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = list()
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j + 1 + length]
            ans.append(word)
            i = j + 1 + length
        return ans