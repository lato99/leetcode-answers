class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr = [0 for i in range(27)]
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')]+=1
            arr[ord(t[i]) - ord('a') ] -= 1
        ans = 0
        for count in arr:
            if count > 0:
                ans += count
        return ans
    
#Time Complexity: The algorithm iterates over characters of string s, which is O(n) time where n is the length of the string s. Then inside the for loop, the operaionts are constant time. So overall the time complexity is O(n).
#Space Complexity: Only data structure that is used is the array that we are storing the occurences of the characters. It has fixed length of 27. So the space complexity is O(1) which is constant space.  