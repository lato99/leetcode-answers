from ast import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = dict()
        for num in arr:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        occurences = []
        for k,v in hm.items():
            if v in occurences:
                return False
            occurences.append(v)
        return True
    #Time Complexity: O(n) where n is the length of the arr list. We iterate over arr list, and do operations on hashmap which cost constant O(1) time. Then we iterate over the hashmap hm which is also O(n) time at worst, which is when every number has unique occurences.
    #Space Complexity: O(n) where n is the length of the arr list. If every element of the arr list is unique, then the hashmap will have O(n) at worst case.
