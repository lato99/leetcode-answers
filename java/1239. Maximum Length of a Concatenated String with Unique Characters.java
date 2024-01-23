import java.util.Arrays;
import java.util.List;

class Solution {
    public int maxLength(List<String> arr) {
        int[] dp = new int[arr.size()];
        Arrays.fill(dp, -1);
        return helper(arr, 0, "",dp);
    }

    public int helper(List<String> arr, int index,String currStr, int[] dp){
        //if index out of range, reutrn current length
        if(index >= arr.size()){
            return currStr.length();
        }
        //if current arr element does not break uniqueness, check max(contain arr[index], currStr)
        int max_len = currStr.length();
        if(isUnique(arr.get(index), currStr)){
            String newStr = currStr + arr.get(index);
            max_len = Math.max(max_len,helper(arr,index+1,newStr,dp));
        }
        //now check previous max and notContain(arr[index])(prevMax, notContain)
        //store in dp[index], return dp[index]
        max_len = Math.max(max_len, helper(arr,index+1,currStr,dp));
        dp[index] = max_len;
        return dp[index];
        

    }
    public boolean isUnique(String str1, String str2){
        for(int i = 0; i < str1.length(); i++){
            String strCheck = String.valueOf(str1.charAt(i));
            if(str2.contains(strCheck)){
                return false;
            }
            else{
                str2 = str2 + strCheck;
            }
        }
        return true;
    }

}