class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dict = dict()
        begin_index = 0
        max_len = 0
        for index, single_s in enumerate(s):
            if single_s in str_dict:
                single_s_index = str_dict[single_s]
                if single_s_index >= begin_index:
                    if index - begin_index > max_len:
                        max_len = index - begin_index
                    begin_index = single_s_index + 1
            if index == len(s) - 1 and not (single_s in str_dict and str_dict[single_s] >= begin_index) and index - begin_index + 1 > max_len:
                max_len = index - begin_index + 1
            str_dict[single_s] = index
        return max_len