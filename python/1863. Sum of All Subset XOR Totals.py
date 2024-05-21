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


# Second Solution - improved time complexity and space complexity
# Time Complexity : O(2^n) where n is the length of nums. Calculating all the subsets will take O(2^n) time.
# Space Complexity : O(n) where n is the length of nums. There are no data structures, the space complexity is determined by the call stack from recursion. The recursion call stack can at most be n.
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.calculateXORSum(nums,0,0)
    def calculateXORSum(self,nums,index,total):
        if index == len(nums):
            return total
        withIndex = self.calculateXORSum(nums,index+1,nums[index] ^ total)
        withoutIndex = self.calculateXORSum(nums,index+1,total)
        return withIndex + withoutIndex
