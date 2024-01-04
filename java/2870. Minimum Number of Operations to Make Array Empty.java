import java.util.HashMap;

class Solution {
    public int minOperations(int[] nums) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for(int num : nums){
            hashMap.compute(num, (key,value) -> (value == null) ? 1 : value + 1);
        }
        int ans = 0;
        for(Integer key : hashMap.keySet()){
            int value = hashMap.get(key);
            if(value == 1){
                return -1;
            }
            else if(value == 2){
                ans++;
            }
            else{
                while(value != 0){
                    if(value%3 == 0){
                        ans+= value/3;
                        break;
                    }
                    else{
                        value-=2;
                        ans+=1;
                    }
                }
            }
        }
        return ans;
    }
}

//Time complexity : O(N), n is the length of the nums array. We iterate over the nums to put the values into the hashmap, then we iterate over the hashmap. In the while loop, the worst case of iteration until breaking out of the while loop is v/2 which is constant O(1). Therefore Time complexity is O(N) in worst case.
// Space complexity : O(N), this is because we put the nums into a hash map, and in worse case every value has one occurence, and in that case, we get O(N) space complexity.
