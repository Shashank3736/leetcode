#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        start_list = [0, 1]
        for i in range(1, n):
            summand = 2**(i)
            start_list = start_list+[elem+summand for elem in reversed(start_list)]
        return start_list

        
# @lc code=end
