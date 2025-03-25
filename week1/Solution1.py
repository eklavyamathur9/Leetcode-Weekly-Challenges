#Solution1 : Count Partitions With Even Sum Difference
class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ts= sum(nums)
        ls=0
        c=0
        for i in range(n-1):
            ls+=nums[i]
            rs=ts-ls
            if abs(ls-rs)%2==0:
                c+=1
        return c