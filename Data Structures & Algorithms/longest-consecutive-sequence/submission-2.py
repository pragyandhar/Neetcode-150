class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = 0
        length = 0

        seen = set(nums)

        for i in seen:
            if i-1 not in seen:
                length = 1
                while i + length in seen:
                    length += 1
                count = max(count, length)

        
        return count
            