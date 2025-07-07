#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#
from typing import List
# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique_num1 = list(set(nums1) - set(nums2))
        unique_num2 = list(set(nums2) - set(nums1))
        return [unique_num1, unique_num2]
        
# @lc code=end

