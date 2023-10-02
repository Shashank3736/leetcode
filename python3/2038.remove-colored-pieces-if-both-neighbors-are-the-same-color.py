#
# @lc app=leetcode id=2038 lang=python3
#
# [2038] Remove Colored Pieces if Both Neighbors are the Same Color
#

# @lc code=start
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0

        for i in range(1, len(colors)-1):
            if colors[i] == 'A' and colors[i-1] == 'A' and colors[i+1] == 'A':
                alice += 1
            elif colors[i] == 'B' and colors[i-1] == 'B' and colors[i+1] == 'B':
                bob += 1
        
        return alice > bob
        
# @lc code=end

