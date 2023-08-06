from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = dict()
        for index, item in enumerate(nums):
            if target - item in result_dict:
                return list((result_dict[target - item], index))
            else:
                result_dict[item] = index