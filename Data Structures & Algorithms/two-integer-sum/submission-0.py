class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0    
        dictionary = dict()

        for i in range(0, len(nums)):
            if (target-nums[i]) in dictionary:
                return [dictionary[target-nums[i]], i]
            dictionary[nums[i]] = i