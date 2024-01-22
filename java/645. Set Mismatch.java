import java.util.HashSet;

class Solution {
    public int[] findErrorNums(int[] nums) {
        HashSet<Integer> hs = new HashSet<Integer>();
        for(int i = 1; i < nums.length+1; i++){
            hs.add(i);
        }
        int[] ans = new int[2];
        for(int i : nums){
            if(hs.contains(i)){
                hs.remove(i);
                }
            else{
                ans[0] = i;
            }
        }
        for(int i : hs){
            ans[1] = i;
        }
        return ans;
    }
}

// Time Complexity O(n) where n is the length of nums list. First we add n elements to the set in O(n) time. Then we iterate over elements of nums and check if it exists in set, checking if exists in set is constant O(1) time. Iterating over nums list is O(n) time. Thus the time complexity of the algorithm is O(n)
// Space Comlexity O(n) where n is the length of the nums list. The set uses extra space of O(n). 
    

// Using math solution
// class Solution {
//     public int[] findErrorNums(int[] nums) {
//         int n = nums.length;
//         int normalSum = n*(n+1) / 2;
//         int mismatchedSum = Arrays.stream(nums).distinct().sum();
//         int missingNumber = normalSum - mismatchedSum;
//         int duplicateNumber = Arrays.stream(nums).sum() - (normalSum - missingNumber);
//         return new int[]{duplicateNumber, missingNumber};
//     }
// }
// Time Complexity is O(n) where n is the length of the nums list. Sum operations are O(n) time. Other operations are simple binary operations with O(1) time.
// Space comlexity is O(1), no data structure used, just variables which are constant space.
// class Solution {
//     public int[] findErrorNums(int[] nums) {
//         int n = nums.length;
//         int[] frequency = new int[n];
//         Arrays.fill(frequency,0);
//         for(int i: nums){
//             frequency[i-1]++;
//         }
//         int missing = -1;
//         int duplicate = -1;
//         for(int i = 0; i < n; i++){
//             if(frequency[i] == 2){
//                 duplicate = i+1;
//             }
//             if(frequency[i] == 0){
//                 missing = i+1;
//             }
//         }
//         return new int[]{duplicate,missing};
//     }
// }