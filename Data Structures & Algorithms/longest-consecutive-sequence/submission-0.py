class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        consecutive_number = 1
        start = 0

        seen = set(nums)

        for i in seen:
            if i-1 not in seen:
                start = i
            if start+consecutive_number in seen:
                count += 1
                consecutive_number += 1
        
        return count+1
            