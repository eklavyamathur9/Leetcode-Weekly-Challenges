#Solution2 : Assign Elements to Groups with Constraints
class Solution(object):
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        a=[]
        for g in groups:
            besti=-1
            for j in range(len(elements)):
                if g % elements[j]==0:
                    besti = j
                    break
            a.append(besti)
        return a
        