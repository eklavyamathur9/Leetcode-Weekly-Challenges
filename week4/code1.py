class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s)>2:
            s1=""
            for x in range(len(s)-1):
                s1=s1+str((int(s[x])+int(s[x+1]))%10)
            s=s1
        return(s[0]==s[1])