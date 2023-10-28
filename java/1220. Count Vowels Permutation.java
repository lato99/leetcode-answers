class Solution {
    public int countVowelPermutation(int n) {
        long a = 1; 
        long e = 1;
        long i = 1;
        long o = 1;
        long u = 1;
        long mod = (long) Math.pow(10,9) + 7;
        for(int x = 1; x < n; x++){
            long new_a = e;
            long new_e = (a+ i) % mod;
            long new_i = (a + e + o + u) % mod;
            long new_o = (i + u) % mod;
            long new_u = a;
            a = new_a;
            e = new_e;
            i = new_i;
            o = new_o;
            u = new_u;
        }
        int x = (int)((a+e+i+o+u) % mod);
        return  x;
    }
}