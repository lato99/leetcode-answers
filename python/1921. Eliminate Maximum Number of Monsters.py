
from ast import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        arrivalTimes = [dist[i]/speed[i] for i in range(n)]
        arrivalTimes = sorted(arrivalTimes)
        index = 0
        while index < n and arrivalTimes[index] - index > 0:
            index += 1
        return min(index , n)
