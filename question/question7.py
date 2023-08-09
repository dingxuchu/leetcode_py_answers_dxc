class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        output = flag * int(str(x)[::-1])
        if output < -(2**31) or output > 2 ** 31 - 1:
            output = 0
        return output