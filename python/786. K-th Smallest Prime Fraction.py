# Time Complexity : O( (n+k) * log(n)) where n is the lenght of arr. Pushing n elements into the heap in the beginning of the algorithm takes n * log(n) time.
# Space Complexity : O(n) where n is the length of the arr. The algorithm uses a heap with length of n, other variables are contants.
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        hq = []
        n = len(arr)
        for i in range(n):
            fraction = arr[i] / arr[n-1]
            heapq.heappush(hq,(fraction,i,n-1))
        while k != 0:
            curr = heapq.heappop(hq)
            frac = curr[0]
            nom = curr[1]
            denom = curr[2]
            if nom + 1 < denom:
                newFrac = arr[nom] / arr[denom-1]
                heapq.heappush(hq,(newFrac,nom,denom-1))
            k -= 1
            if k==0:
                return [arr[nom],arr[denom]]
        return [-1,-1]