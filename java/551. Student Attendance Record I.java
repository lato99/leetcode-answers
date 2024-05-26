//git  Time Complexity : O(n) where n is the length of s. s string is traversed once, if two characters are 'A' or there exists 3 consecutive 'L', the algorithm terminates. In worst case we traverse the string to the end, TimeComplexity is O(n).
// Space Complexity : O(1), there are no data structures used in the problem. Only constants for keeping track of total absent days and consecutive late days.
class Solution {
    public boolean checkRecord(String s) {
        int absentDaysCount = 0;
        int consecutiveLateDaysCount = 0;
        for(int i = 0; i < s.length() ; i++){
            char currChar = s.charAt(i);
            if(currChar == 'A'){
                if(++absentDaysCount >= 2){
                    return false;
                }
            }
            if(currChar == 'L'){
                if(++consecutiveLateDaysCount >= 3){
                    return false;
                }
            }
            if(currChar != 'L'){
                consecutiveLateDaysCount = 0;
            }
        }
        return true;
    }
}