from ast import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        st = set()
        for i in range(len(nums)):
            st.add(i+1)
        ans = []
        for i in nums:
            if i in st:
                st.remove(i)
            else:
                ans.append(i)
        ans.append(st.pop())
        return ans
# Time Complexity O(n) where n is the length of nums list. First we add n elements to the set in O(n) time. Then we iterate over elements of nums and check if it exists in set, checking if exists in set is constant O(1) time. Iterating over nums list is O(n) time. Thus the time complexity of the algorithm is O(n)
# Space Comlexity O(n) where n is the length of the nums list. The set uses extra space of O(n). 
    

## Using math solution
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
       n = len(nums)
       #difference between normal nums and set(mismatchedSum) will give missing number
       normalSum = n*(n+1)//2
       missingNum = normalSum - sum(set(nums))
       duplicateNum = sum(nums) - (normalSum - missingNum)
       return [duplicateNum,missingNum]
# Time Complexity is O(n) where n is the length of the nums list. Sum operations are O(n) time. Other operations are simple binary operations with O(1) time.
# Space comlexity is O(1), no data structure used, just variables which are constant space.