class Solution {
    public int minSteps(String s, String t) {
        int[] map = new int[27];
        for(int i = 0; i < s.length(); i++){
            int sOrd = (int) s.charAt(i) - 'a';
            int tOrd = (int) t.charAt(i) - 'a';
            map[sOrd] += 1;
            map[tOrd] -= 1;
        }
        int ans = 0;
        for(int i : map){
            ans += Math.max(i,0);
        }
        return ans;
    }
}

//Time Complexity: The algorithm iterates over characters of string s, which is O(n) time where n is the length of the string s. Then inside the for loop, the operaionts are constant time. So overall the time complexity is O(n).
//Space Complexity: Only data structure that is used is the array that we are storing the occurences of the characters. It has fixed length of 27. So the space complexity is O(1) which is constant space.  