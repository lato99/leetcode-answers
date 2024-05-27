// Time Complexity : O(n logn), where n is the length of nums. Sorting takes O(n logn) time. After sorting, the nums array is traversed, with constant time operations. So traversing the nums array takes O(n) time. Overall time complexity is O(n logn) time.
// Space Complexity : O(n logn), sorting takes O(n logn) time, and there are no other data structure used except constants. 

class Solution {
    public int specialArray(int[] nums) {
        int currMax = -1;
        Arrays.sort(nums);
        int l = nums.length;
        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            if(nums[i] >= l && currMax < l){
                return l;
            }
            l--;
            currMax = num;
        }
        return -1;
    }
}