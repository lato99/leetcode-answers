from ast import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [-1 for i in range(len(arr))]
        return self.helper(arr,0,dp,set(), "")
    def helper(self, arr, index, dp, store, currStr):
        if index >= len(arr):
            return len(currStr)
        else:
            notContain = self.helper(arr,index+1,dp,store.copy(),currStr)
            contain = len(currStr)
            isUnique = True
            tempStore = store.copy()
            tempCurrStr = currStr
            for ch in arr[index]:
                if ch in tempStore:
                    isUnique = False
                    break
                else:
                    tempStore.add(ch)
                    tempCurrStr += ch
            if isUnique:
                contain = self.helper(arr,index+1,dp,tempStore, tempCurrStr)
            len1 = notContain
            len2 = contain
            len3 = len(currStr)
            if len1 >= len2 and len1 >= len3:
                dp[index] = len1
                return dp[index]
            elif len2 >= len1 and len2 >= len3:
                dp[index] = len2
                return dp[index]
            else:
                dp[index] = len3
                return dp[index]

# Time Complexity is O(2^n) where n is the length of arr. With dp, we use bottom up (tabulation), and the recursion depth is O(n), and we use recursion in two different brancehs, one with containing the current index, and without containing the current index, so the time complexity becomes O(2^n).
# Space Complexity is O(n) where n is the length of the 