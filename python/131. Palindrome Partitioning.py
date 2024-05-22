# The time complexity of the given solution for finding all possible palindrome partitions of a string is O(n * 2^n), where n is the length of the input string. This complexity arises because the algorithm explores all possible partitions, which are 2^n-1 in number, and for each partition, it checks if each substring is a palindrome, requiring O(n) time for each check. Consequently, the exponential number of possible partitions combined with the linear time for palindrome verification leads to the overall O(n * 2^n) time complexity.
# The space complexity of the given algorithm is primarily determined by the storage of all possible palindromic partitions and the recursive call stack. The result list `self.allPalindromes` can store up to 2^(n-1) partitions, with each partition containing up to n substrings, leading to O(n * 2^n) space in the worst case. Additionally, the recursive call stack can reach a depth of n, contributing O(n) space. Temporary data structures like `currPalindrome` and the recursive palindrome checks also use O(n) space. Thus, the overall space complexity, dominated by the result storage, is O(n * 2^n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.allPalindromes = []
        self.helper([],s)
        return self.allPalindromes
    def helper(self,currPalindrome, s):
        if len(s) == 0:
            self.allPalindromes.append(currPalindrome[:])
            return
        for i in range(len(s)):
            firstHalf = s[0:i+1]
            if self.isPalindrome(s,0,len(firstHalf)-1):
                currPalindrome.append(firstHalf)
                self.helper(currPalindrome, s[i+1:])
                currPalindrome.pop()

    
    def isPalindrome(self,s,i,j):
        if i>j:
            return True
        elif i == j:
            return s[i] == s[j]
        else:
            return s[i] == s[j] and self.isPalindrome(s,i+1,j-1)

