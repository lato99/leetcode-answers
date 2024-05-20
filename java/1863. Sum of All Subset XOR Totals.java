# Time Complexity: O(2^n * n) where n is the length of nums. in generateSubsets function, function itself is called recursively with backtracking. Element from nums is added, function is called, then the elemetn is popped and function is called again. This takes O(2^n) time. xorSum iterates over all the subsets, then with xor operation sums them up. Average subset has length n/2. Thus, iterating over 2^n array and summing up n/2 elements will take O(n * 2^n) time.
# Space Complexity: O(2^n * n) where n is the length of nums. The list which all the subsets are stored will have 2^n elements. And the average length of each element is n, thus it will have O(2^n * n) space. The call stack by the recursion can have O(n) space at most.
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        allSubsets = [] 
        self.generateSubsets(0,nums,[],allSubsets)
        total = self.xorSum(allSubsets)
        print(allSubsets)
        return total
    def generateSubsets(self, index, nums, subset,subsets):
        if index == len(nums):
            subsets.append(subset[:])
            return
        subset.append(nums[index])
        self.generateSubsets(index+1,nums,subset,subsets)
        subset.pop()
        self.generateSubsets(index+1,nums,subset,subsets)
    def xorSum(self,subsets):
        total = 0
        for subset in subsets:
            currTotal = 0
            for num in subset:
                currTotal ^= num
            total += currTotal
        return total


