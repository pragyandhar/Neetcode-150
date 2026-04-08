class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set(nums)
        if len(unique_values) == len(nums):
            return False
        return True
        