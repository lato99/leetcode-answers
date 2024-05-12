# Time Complexity : O(n) where n is the length of the input word. The algorithm first traverse the word, until the character ch is found, which in worst case takes O(n) time. Then if found, it reverses the substring from 0 index to found ch index, which also takes O(n) time in worst case.
# Space Complexity : O(n) because in python strings are immutable, and to reverse the string, it should be first turned into a list, which takes O(n) space.
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverseIndex = -1
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                    reverseIndex = i
                    break
        if reverseIndex == -1:
            return "".join(word)
        startIndex = 0
        while reverseIndex > startIndex:
            temp = word[startIndex]
            word[startIndex] = word[reverseIndex]
            word[reverseIndex] = temp
            reverseIndex -= 1
            startIndex += 1
        return "".join(word)
        

