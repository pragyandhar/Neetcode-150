class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n+1)]

        freq = Counter(nums)

        for element, frequency in freq.items():
            bucket[frequency].append(element)

        ans = list()
        for i in range(n, 0, -1):
            ans.extend(bucket[i])
            if len(ans) == k:
                return ans
        