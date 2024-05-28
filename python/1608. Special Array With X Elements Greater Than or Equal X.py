# Time Complexity : O(n logn), where n is the length of nums. Sorting takes O(n logn) time. After sorting, the nums array is traversed, with constant time operations. So traversing the nums array takes O(n) time. Overall time complexity is O(n logn) time.
#  Space Complexity : O(n logn), sorting takes O(n logn) time, and there are no other data structure used except constants. 

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        lastMax = -1
        l = len(nums)
        for i in nums:
            if i >= l and l > lastMax:
                return l
            else:
                l -= 1
            lastMax = i
        return -1