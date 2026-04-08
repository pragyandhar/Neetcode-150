class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = Counter(s)

        for element in t:
            if element in freq:
                freq[element] = freq.get(element, 0) - 1
        
        return all(v == 0 for v in freq.values())