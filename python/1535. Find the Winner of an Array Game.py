class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        l = arr[0]
        winStreak = 0
        for i in range(1,len(arr)):
            r = arr[i]
            if l > r:
                winStreak += 1
            else:
                winStreak = 1
                l = r
            if winStreak == k:
                return l
        return l
