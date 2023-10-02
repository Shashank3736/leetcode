/*
 * @lc app=leetcode id=89 lang=java
 *
 * [89] Gray Code
 */

// @lc code=start

import java.util.ArrayList;

class Solution {
    public List<Integer> grayCode(int n) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        arr.add(0);
        arr.add(1);
        
        for(int i=1; i<n; i++) {
            int sum = (int) Math.pow(2, i);

            for (int j=arr.size()-1;j>=0;j--) {
                arr.add(arr.get(j) + sum);
            }
        }

        return arr;
    }
}
// @lc code=end

