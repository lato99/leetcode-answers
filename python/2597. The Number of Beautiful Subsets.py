# Time Complexity : O(2^n) where n is the lenght of nums. Every subset of the nums array is derived, and constant time operation is done on the array. Sorting the nums array's time complexity depends on the language, but worst case is O(n logn). So time complexity is determined by finding the subsetsi which takes O(2^n) time.
# Space Complexity : O(n) since we have backtracking with recursion, the recursion call stack can be at most O(n) space. Another data structure that is used in the algorithm is freq array, which can have at most n elements in it. Therefore the space complexity is O(n).
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        return self.helper(nums,0,k,[]) - 1  
    def helper(self,nums,i,k,freq):
        if i == len(nums):
            return 1
        total_count = self.helper(nums,i+1,k,freq)
        if nums[i] - k not in freq:
            freq.add(nums[i])
            total_count += self.helper(nums,i+1,k,freq)
            freq.remove(nums[i])
        return total_count