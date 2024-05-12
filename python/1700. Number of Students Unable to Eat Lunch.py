# Space Complexity: Constant Space, O(1). Only two lists with constant space, length of two, are used. There are no other data structures or recursion stack that uses space in the algorithm.
# Time Complexity: O(n) where n is the length of students array. First the studentTypeCounts and sandwichesTypeCounts arrays are filled by traversing the students and sandwiches lists. Then sandwiches list is traversed again to check if there are any students that like the same sandwich type that is on the top of the sandwich stack. Thus, the overall time complexity is O(n). 
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentTypeCounts = [0,0]
        sandwichesTypeCounts = [0,0]
        n = len(students)
        for i in range(n):
            studentTypeCounts[students[i]] += 1
            sandwichesTypeCounts[sandwiches[i]] += 1
        for i in range(n):
            sandwichType = sandwiches[i]
            if studentTypeCounts[sandwichType] == 0:
                return studentTypeCounts[1 - sandwichType]
            else:
                studentTypeCounts[sandwichType] -= 1
        return 0
    

# Intuition:
# Implementation: git