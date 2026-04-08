class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()
        for string in strs:
            sorted_str = "".join(sorted(string))
            dictionary.setdefault(sorted_str, []).append(string)
        return list(dictionary.values())