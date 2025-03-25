#Solution1 : Maximum Difference Between Even and Odd Frequency I
class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        f={}
        for c in s:
            if c in f:
                f[c]+=1
            else:
                f[c]=1
        of=[]
        ef=[]
        for count in f.values():
            if count%2==0:
                ef.append(count)
            else:
                of.append(count)
        if not of or not ef:
            return 0
        return max(of)-min(ef)