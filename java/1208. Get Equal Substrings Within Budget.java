// Time Complexity : O(n) where n is the length of string s. With for loop string s and t is iterated over the characters. At each iteration, constant time comparing operations are done. 
// Space Complexity : O(1) since there are no data structures or any other ... used, only variables. Hence the space complexity is O(1).
class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int maxLen = 0;
        int currCost = 0;
        int start = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == t.charAt(i)){
                maxLen = Math.max(maxLen, i - start + 1);
                continue;
            }
            int newCost = Math.abs((int) s.charAt(i) - (int) t.charAt(i));
            currCost += newCost;
            while(currCost > maxCost){
                currCost -= Math.abs((int) s.charAt(start) - (int) t.charAt(start));
                start++;
            }
            maxLen = Math.max(maxLen, i - start + 1);
        }
        return maxLen;
    }
    
}