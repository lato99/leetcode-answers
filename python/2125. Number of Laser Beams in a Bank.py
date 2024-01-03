from ast import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        countLaser = 0
        prevBeam = 0
        for arr in bank:
            currBeam = self.getNoBeam(arr)
            if currBeam == 0:
                continue
            elif prevBeam == 0:
                prevBeam = currBeam
            else:
                countLaser += (prevBeam * currBeam)
                prevBeam = currBeam
        return countLaser
    
    def getNoBeam(self, bankRow : str) -> int:
        noBeam = 0
        for ch in bankRow:
            if ch=="1":
                noBeam += 1
        return noBeam