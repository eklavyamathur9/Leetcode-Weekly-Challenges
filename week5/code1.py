class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive_set = {num for num in nums if num > 0}
        if positive_set:
            return sum(positive_set)
        else:
            return max(nums)