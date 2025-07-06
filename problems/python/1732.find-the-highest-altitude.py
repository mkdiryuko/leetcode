#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#
from typing import List
# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_point = 0
        point = 0
        for i in range(len(gain)):
            point += gain[i]
            highest_point = max(point, highest_point)
        return highest_point
# @lc code=end

