#Solution3 : Count Substrings Divisible By Last Digit
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        n=len(s)
        for i in range(n):
            num=0
            for j in range(i,n):
                num=num*10+int(s[j])
                ld= int(s[j])
                if ld!=0 and num % ld ==0:
                    count+=1
        return count
  