/*
 * @lc app=leetcode id=2038 lang=java
 *
 * [2038] Remove Colored Pieces if Both Neighbors are the Same Color
 */

// @lc code=start
class Solution {
    public boolean winnerOfGame(String colors) {
        int alice = 0;
        int bob = 0;

        for (int i=1; i < colors.length() - 1; i++) {
            if ((colors.charAt(i) == colors.charAt(i-1)) && (colors.charAt(i) == colors.charAt(i+1)) && (colors.charAt(i) == 'A')) {
                alice++;
            } else if ((colors.charAt(i) == colors.charAt(i-1)) && (colors.charAt(i) == colors.charAt(i+1)) && (colors.charAt(i) == 'B')) {
                bob++;
            }
        }

        return alice > bob;
    }
}
// @lc code=end

