class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a bucket
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        # Create a frequency array
        freq = Counter(nums)
        # Fill the bucket
        for element, frequency in freq.items():
            bucket[frequency].append(element)
        # Iterate from right to left and return the answer
        ans = list()
        for i in range(n, 0, -1):
            ans.extend(bucket[i])
            if len(ans) == k:
                return ans
        