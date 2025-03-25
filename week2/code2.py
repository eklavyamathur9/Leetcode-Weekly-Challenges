#Solution2 : Maximum Manhattan Distance After K Changes
class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        x,y= 0,0
        md = 0
        for i, c in enumerate(s, 1):
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c=="W":
                x -= 1
            cm = abs(x) + abs(y)
            candidate = min(cm + 2 * k, i)
            if candidate > md:
                md = candidate
        return md