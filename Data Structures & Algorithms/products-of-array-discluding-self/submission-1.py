class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        # Counting the zeros else calculating the total product
        for element in nums:
            if element == 0:
                zero_count += 1
            else:
                total_product *= element

        answer = []
        # Basic Checks
        for element in nums:
            if zero_count > 1:
                answer.append(0)
            elif zero_count == 1:
                answer.append(total_product if element == 0 else 0)
            elif zero_count == 0:
                answer.append(total_product // element)
        
        return answer