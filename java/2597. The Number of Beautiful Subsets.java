// Time Complexity : O(2^n) where n is the lenght of nums. Every subset of the nums array is derived, and constant time operation is done on the array. Sorting the nums array's time complexity depends on the language, but worst case is O(n logn). So time complexity is determined by finding the subsetsi which takes O(2^n) time.
// Space Complexity : O(n) since we have backtracking with recursion, the recursion call stack can be at most O(n) space. Another data structure that is used in the algorithm is freq array, which can have at most n elements in it. Therefore the space complexity is O(n).
class Solution {
    public int beautifulSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        return helper(nums,0,k,new HashMap<Integer, Integer>()) - 1;
    }
    public int helper(int[] nums, int i, int k,HashMap<Integer, Integer> hm){
        if(nums.length == i){
            return 1;
        }
        int total_count = helper(nums, i+1, k, hm);
        if( !(hm.getOrDefault(nums[i]-k,0) > 0)){
            hm.put(nums[i],hm.getOrDefault(nums[i],0)+1);
            total_count += helper(nums, i+1,k,hm);
            hm.put(nums[i],hm.getOrDefault(nums[i],0)-1);
        }
        return total_count;
    }
}