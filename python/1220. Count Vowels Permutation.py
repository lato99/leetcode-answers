class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        a, e, i,o, u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            n_a = e
            n_e = (a + i) % mod
            n_i = (a + e + o + u) % mod
            n_o = (i + u) % mod
            n_u = a

            a = n_a
            e = n_e
            i = n_i
            o = n_o
            u = n_u
        
        return (a+e+i+o+u) % mod
