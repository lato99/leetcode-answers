# Time Complexity : O(n) where n is the parameter n of minPatches function. In worst case, while loop iterates n times, and at each iteration, if else statements have constant time operations.
# Space Complexity : O(1), no extra space is used. Just O(1) space constants.
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missingNumber = 1
        patchCount = 0
        i = 0
        while missingNumber <= n:
            if i >= len(nums):
                patchCount += 1
                missingNumber *= 2
            else:
                num = nums[i]
                if num <= missingNumber:
                    missingNumber += nums[i]
                    i += 1
                else:
                    patchCount += 1
                    missingNumber *= 2
        return patchCount