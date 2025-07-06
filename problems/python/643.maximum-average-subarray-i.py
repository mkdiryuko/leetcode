#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
from typing import List

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
# @lc code=end
