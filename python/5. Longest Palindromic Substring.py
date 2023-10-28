class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longestPal = ""
        lenLongest = -1
        for i in range(n):
             #odd case
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                curr_len = r-l+1
                if curr_len > lenLongest:
                    longestPal = s[l:r+1]
                    lenLongest = curr_len
                l -= 1
                r += 1
            #even case
            l, r = i , i+1
            while l >= 0 and r < n and s[l] == s[r]:
                curr_len = r-l+1
                if curr_len > lenLongest:
                    longestPal = s[l:r+1]
                    lenLongest = curr_len
                l -= 1
                r += 1
        return longestPal


