import java.util.*;

class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();
        int maxSize = 1;
        for(int num: nums){
            hm.put(num,hm.getOrDefault(num,0)+1);
            maxSize = Math.max(maxSize,hm.get(num));
        }
        for(int i = 0; i < maxSize; i++){
            List<Integer> temp = new ArrayList<>();
            ans.add(temp);
        }
        for(int key: hm.keySet()){
            int val = hm.get(key);
            for(int i = 0; i < val; i++){
                ans.get(i).add(key);
            }
        }
        return ans;
    }
}