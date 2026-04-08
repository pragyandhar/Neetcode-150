class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        seen = set()
        for i in range (0, len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        '''

        unique_values = set(nums)
        if len(unique_values) == len(nums):
            return False
        return True
        