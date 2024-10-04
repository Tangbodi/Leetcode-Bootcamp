class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, answer = [0] * length, [0] * length, [0] * length
        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]
        for i in range(length):
            answer[i] = left[i] * right[i]
        return answer