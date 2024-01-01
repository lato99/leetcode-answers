import java.util.Arrays;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int noContentChildren = 0;
        int sIndex = 0;
        while(noContentChildren < g.length && sIndex < s.length){
            int contentSize = g[noContentChildren];
            int cookieSize = s[sIndex];
            if(contentSize <= cookieSize){
                noContentChildren++; sIndex++;
            }
            else{
                sIndex++;
            }
        }
        return noContentChildren;
    }
}