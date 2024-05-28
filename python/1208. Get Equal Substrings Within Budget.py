# Time Complexity : O(n) where n is the length of string s. With for loop string s and t is iterated over the characters. At each iteration, constant time comparing operations are done. 
# Space Complexity : O(1) since there are no data structures or any other ... used, only variables. Hence the space complexity is O(1).
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = len(s)
        maxLen = 0
        currLen = 0
        start = 0
        cost = 0
        for i in range(l):
            if s[i] == t[i]:
                currLen+=1
            else:
                newCost = abs(ord(s[i]) - ord(t[i]))
                while cost + newCost > maxCost:
                    cost -=  abs(ord(s[start]) - ord(t[start]))
                    start += 1
                    currLen -= 1
                
                currLen += 1
                cost += newCost
            maxLen = max(maxLen,currLen)
        return maxLen
            