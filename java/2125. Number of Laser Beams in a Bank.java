class Solution {
    public int numberOfBeams(String[] bank) {
        int prevRowBeams = 0;
        int ans = 0;
        for(String row: bank){
            int curRowBeams = getNumberOfBeams(row);
            if(curRowBeams == 0){
                continue;
            }
            else if(prevRowBeams == 0){
                prevRowBeams = curRowBeams;
            }
            else{
                ans += (prevRowBeams * curRowBeams);
                prevRowBeams = curRowBeams;
            }
        }
        return ans;
    }

    public int getNumberOfBeams(String bankRow){
        int ans = 0;
        for(int i = 0; i < bankRow.length() ; i++){
            if(bankRow.charAt(i) == '1'){
                ans++;
            }
        }
        return ans;
    }
}