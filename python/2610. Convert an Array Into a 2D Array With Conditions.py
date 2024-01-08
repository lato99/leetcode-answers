from ast import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_map = dict()
        size = 1
        for num in nums:
            if num in hash_map:
                temp = hash_map[num]
                hash_map[num] = temp+1
                size = max(size,temp+1)
            else:
                hash_map[num] = 1
        ret = [[] for i in range(size)]
        for k,v in hash_map.items():
            for i in range(v):
                ret[i].append(k)
        return ret
        