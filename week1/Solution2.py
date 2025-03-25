#Solution2 : Maximum Frequency After Subarray Operation
class Solution:
    def maxFrequency(self, nums,k):
        n = len(nums)
        kcount = 0 
        for x in nums:
            if x==k:
                kcount+=1
        answer = kcount
        for x in range(1, 51):
            curr_k = 0 
            my_min = 0
            xcount = 0 
            for i in range(n):
                if nums[i]==x:
                    xcount+=1 
                if nums[i]==k:
                    curr_k+=1
                my_min = min(my_min, xcount-curr_k)
                answer = max(answer, xcount-my_min+kcount-curr_k) 
        return answer