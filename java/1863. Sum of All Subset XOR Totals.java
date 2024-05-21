//  Time Complexity: O(2^n * n) where n is the length of nums. in generateSubsets function, function itself is called recursively with backtracking. Element from nums is added, function is called, then the elemetn is popped and function is called again. This takes O(2^n) time. xorSum iterates over all the subsets, then with xor operation sums them up. Average subset has length n/2. Thus, iterating over 2^n array and summing up n/2 elements will take O(n * 2^n) time.
//  Space Complexity: O(2^n * n) where n is the length of nums. The list which all the subsets are stored will have 2^n elements. And the average length of each element is n, thus it will have O(2^n * n) space. The call stack by the recursion can have O(n) space at most.
class Solution {
    public int subsetXORSum(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        findAllSubsets(subsets,new ArrayList<Integer>(), nums,0);
        System.out.println(subsets);
        return addAllElements(subsets);    
        }
    public int addAllElements(List<List<Integer>> subsets){
        int total = 0;
        for(List<Integer> subset : subsets){
            int currTotal = 0;
            for(int num : subset){
                currTotal ^= num;
            }
            total += currTotal;
        }
        return total;
    }
    public void findAllSubsets(List<List<Integer>> subsets, List<Integer> subset, int[] nums, int index){
        if(index == nums.length){
            subsets.add( new ArrayList<>(subset));
            return;
        }
         subset.add(nums[index]);

        findAllSubsets(subsets, subset,nums,index+1);
       subset.remove(subset.size() - 1);
        findAllSubsets(subsets, subset,nums,index+1);
    }
}


//  Second Solution - improved time complexity and space complexity
//  Time Complexity : O(2^n) where n is the length of nums. Calculating all the subsets will take O(2^n) time.
//  Space Complexity : O(n) where n is the length of nums. There are no data structures, the space complexity is determined by the call stack from recursion. The recursion call stack can at most be n.
class Solution {
    public int subsetXORSum(int[] nums) {
        return helper(nums,0,0);
    }
    public int helper(int[] nums, int index,int total){
        if(index == nums.length){
            return total;
        }
        int withCount = helper(nums,  index+1, total^nums[index]);
        int withoutCount = helper(nums,  index+1,total);
        return withCount + withoutCount;
    }
}