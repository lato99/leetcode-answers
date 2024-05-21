// Time Complexity : O(2^n) where n is the length of nums. There are 2^n possible subsets for any given array. in getSubsets function, it is recursively called 2 times, once with unmodified array, once with modified subset array. The function is called 2^n times, with O(1) time operations. So the overal time complexity is O(2^n).
// Space Complexity : O(n * 2^n) where n is the length of nums. All possible subsets are stored in an array, which has 2^n elements, and average length for each of the array is n/2. The call stack from the recursive function has length of n in worst case. So the overall space complexity is O(n * 2^n) due to the array we store the subsets. 
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        getSubsets(nums,0,new ArrayList<Integer>(), subsets);
        return subsets;
    }
    public void getSubsets(int[] nums, int index, List<Integer> subset, List<List<Integer>> subsets){
        if(index == nums.length){
            subsets.add(new ArrayList<Integer>(subset));
            return;
        }
        subset.add(nums[index]);
        getSubsets(nums,index+1,subset,subsets);
        subset.remove(subset.size()-1);
        getSubsets(nums,index+1,subset,subsets);
    }
}