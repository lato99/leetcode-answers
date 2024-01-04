class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #put num, occurence into hash_map
        hash_map = dict()
        ans = 0
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        #iterate through hash_map, get operation count
        for k,v in hash_map.items():
            if v == 1:
                return -1
            elif v == 2:
                ans += 1
            else:
                while v != 0:
                    if v % 3 == 0:
                        ans += (v/3)
                        break
                    else:
                        ans += 1
                        v -=2
        if ans == 0:
            return -1
        return int(ans)


# Time complexity : O(N), n is the length of the nums array. We iterate over the nums to put the values into the hashmap, then we iterate over the hashmap. In the while loop, the worst case of iteration until breaking out of the while loop is v/2 which is constant O(1). Therefore Time complexity is O(N) in worst case.
# Space complexity : O(N), this is because we put the nums into a hash map, and in worse case every value has one occurence, and in that case, we get O(N) space complexity.

