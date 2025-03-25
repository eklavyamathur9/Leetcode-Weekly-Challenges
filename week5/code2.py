class Solution(object):
    def beautifulNumbers(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        def isb(n):
            digits=[int(d) for d in str(n)]
            digitsum=sum(digits)
            digitproduct =1 
            for d in digits:
                digitproduct*=d
            return digitsum!=0 and digitproduct%digitsum==0
        count=0
        for num in range(l,r+1):
            if isb(num):
                count+=1
        return count