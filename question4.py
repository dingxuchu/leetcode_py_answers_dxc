from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_result = 0
        nums_len1 = len(nums1)
        nums_len2 = len(nums2)
        all_len = nums_len1 + nums_len2
        odd_flag = all_len % 2
        if odd_flag:
            median_index = all_len // 2
        else:
            median_index = all_len // 2 - 1
        count_index = -1
        begin_index1 = 0
        begin_index2 = 0
        while begin_index1 < nums_len1 or begin_index2 < nums_len2:
            if begin_index1 < nums_len1 and begin_index2 < nums_len2:
                if nums1[begin_index1] > nums2[begin_index2]:
                    tmp_value = nums2[begin_index2]
                    begin_index2 += 1
                else:
                    tmp_value = nums1[begin_index1]
                    begin_index1 += 1
            elif begin_index1 == nums_len1:
                tmp_value = nums2[begin_index2]
                begin_index2 += 1
            else:
                tmp_value = nums1[begin_index1]
                begin_index1 += 1
            count_index += 1
            if median_index == count_index:
                median_result = tmp_value
                if odd_flag:
                    return median_result
            if not odd_flag and median_index + 1 == count_index:
                median_result = (median_result + tmp_value) / 2
                return median_result