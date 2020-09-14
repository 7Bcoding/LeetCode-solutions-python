class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 解法：长除法
        # 需要用一个哈希表记录余数出现在小数部分的位置，当你发现已经出现的余数，就可以将重复出现的小数部分用括号括起来。
        # 再出发过程中余数可能为 0，意味着不会出现循环小数，立刻停止程序。
        # 测试样例情况：
        # 0 / 1  --------- 被除数为 0。
        # 1 / 0  --------- 除数为 0，应当抛出异常，这里为了简单起见不考虑。
        # 20 // 4  ------- 答案是整数，不包括小数部分。
        # 1 / 2  --------- 答案是 0.5，是有限小数。
        # -1/4 or 1/-4  -- 除数被除数有一个为负数，结果为负数。
        # -1/-4  --------- 除数和被除数都是负数，结果为正数。
        # −2147483648 /-1 -- 转成整数时注意可能溢出。

        num = abs(numerator)
        dem = abs(denominator)  # python对于负数的除法依然是向下取整，题中的要求是按照绝对值除法余数的，所以取绝对值

        flag = 1 if num * dem >= 0 else -1  # 数字的整体符号
        head = num // dem
        head = str(head) if flag > 0 else '-' + str(head)  # 整数部分

        rem = num % dem
        dec = []
        remain = {}             # 用字典计算非循环部分余数出现的最后一次位置
        ind = 0

        # 余数为 0 时除尽了,退出循环，当除不尽时，一旦发生了重复代表从余数上一次在字典中记录的位置开始发生了循环，这部分即为循环小数
        while rem != 0 and rem not in remain:
            remain[rem] = ind
            rem *= 10
            dec.append(str(rem // dem))
            rem = rem % dem
            ind += 1

        if not dec:
            return head
        if rem == 0:
            return head + '.' + ''.join(dec)
        else:
            return head + '.' + ''.join(dec[:remain[rem]]) + '(' + ''.join(dec[remain[rem]:]) + ')'
