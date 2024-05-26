# Time Complexity : O(n) where n is the length of s. s string is traversed once, if two characters are 'A' or there exists 3 consecutive 'L', the algorithm terminates. In worst case we traverse the string to the end, TimeComplexity is O(n).
# Space Complexity : O(1), there are no data structures used in the problem. Only constants for keeping track of total absent days and consecutive late days.
class Solution:
    def checkRecord(self, s: str) -> bool:
        consecutiveLateDays = 0
        totalAbsentDays = 0
        for i in s:
            if i == "A":
                totalAbsentDays += 1
                if totalAbsentDays > 1:
                    return False
            elif i == "L":
                consecutiveLateDays += 1
                if consecutiveLateDays > 2:
                    return False
            if i != "L":
                consecutiveLateDays = 0
        return True