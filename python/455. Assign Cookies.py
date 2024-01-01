from ast import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gSorted, sSorted = sorted(g), sorted(s)
        l,r = 0, 0
        noContentChildren = 0
        while(l < len(gSorted) and r < len(sSorted)):
            gSize = gSorted[l]
            sSize = sSorted[r]
            if(gSize <= sSize):
                l+=1
                r+=1
                noContentChildren+=1
            else:
                r += 1
        return noContentChildren