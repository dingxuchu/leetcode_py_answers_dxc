class Solution:
    def myAtoi(self, s: str) -> int:
        output_str = ''
        flag = 0
        for single_s in s:
            if flag == 0 and single_s == "-":
                flag = -1
                continue
            elif flag == 0 and single_s == "+":
                flag = 1
                continue
            elif flag == 0 and single_s == " ":
                continue
            elif single_s in ("0123456789"):
                if flag == 0:
                    flag = 1
                output_str += single_s
            else:
                break
        if len(output_str) == 0:
            output_num = 0
        else:
            output_num = int(output_str) * flag
        if output_num < -(2**31):
            output_num = -(2**31)
        if output_num > 2 ** 31 - 1:
            output_num = 2 ** 31 - 1
        return output_num