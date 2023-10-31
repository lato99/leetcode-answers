class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ret = sorted(arr,key = lambda x: (Solution.countBits(x),x))
        return ret
    def countBits(num):
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
                num -= 1
            else:
                num /= 2
        return count



#Using built in function bin()
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         ret = sorted(arr,key = lambda x: (bin(x).count('1'),x))
#         return ret
