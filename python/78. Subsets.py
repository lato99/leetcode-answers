# Time Complexity : O(2^n) where n is the length of nums. There are 2^n possible subsets for any given array. in getSubsets function, it is recursively called 2 times, once with unmodified array, once with modified subset array. The function is called 2^n times, with O(1) time operations. So the overal time complexity is O(2^n).
# Space Complexity : O(n * 2^n) where n is the length of nums. All possible subsets are stored in an array, which has 2^n elements, and average length for each of the array is n/2. The call stack from the recursive function has length of n in worst case. So the overall space complexity is O(n * 2^n) due to the array we store the subsets. 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.getSubsets(nums,[],subsets,0)
        return subsets
    def getSubsets(self, nums, subset, subsets, index):
        if index == len(nums):
            subsets.append(subset[:])
            return
        subset.append(nums[index])
        self.getSubsets(nums,subset,subsets,index+1)
        subset.pop()
        self.getSubsets(nums,subset,subsets,index+1)