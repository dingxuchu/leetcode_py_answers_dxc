class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        str_list = ["" for x in range(numRows)]
        i, flag = 0, -1
        for single_s in s:
            str_list[i] += single_s
            if i == 0 or i == numRows - 1:
                flag = - flag
            i += flag
        return "".join(str_list)