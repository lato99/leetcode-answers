class Solution {
    public int getWinner(int[] arr, int k) {
        int left = 0;
        int right = 1;
        int winCount = 0;
        while(right < arr.length){
            int l = arr[left];
            int r = arr[right];
            if( l > r){
                winCount+=1;
                right += 1;
            }
            else{
                winCount = 1;
                left = right;
                right = left + 1;
            }
            if(winCount == k){
                return arr[left];
            }
        }
        return arr[left];
    }
}