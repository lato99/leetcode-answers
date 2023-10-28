class Solution {
    public String longestPalindrome(String s) {
        int lenS = s.length();
        int lenLongestPal = -1;
        String longestPal = "";
        for(int i = 0; i < lenS; i++){
            //odd case
            int left = i;
            int right = i;
            while( left >= 0 && right < lenS && s.charAt(left) == s.charAt(right)){
                int curr_len = right - left + 1;
                if(curr_len > lenLongestPal){
                    longestPal = s.substring(left, right + 1);
                    lenLongestPal = curr_len;
                }
                left -= 1;
                right += 1;
            }
            //even case
            left = i;
            right = i+1;
            while(left >= 0 && right < lenS &&  s.charAt(left) == s.charAt(right)){
                int curr_len = right - left + 1;
                if( curr_len > lenLongestPal){
                    longestPal = s.substring(left, right + 1);
                    lenLongestPal = curr_len;
                }
                left -= 1;
                right += 1;
            }
        }
        return longestPal;
        
    }
}