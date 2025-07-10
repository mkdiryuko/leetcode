#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from typing import List
# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dic = {}
        for num in arr:
            count_dic[num] = count_dic.get(num, 0) + 1
        return len(count_dic) == len(set(count_dic.values()))
        
# @lc code=end

