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

        flag = 1 if numerator * denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)  # python对于负数的除法依然是向下取整，题中的要求是按照绝对值除法余数的，所以取绝对值

        head = numerator // denominator
        head = str(head) if flag > 0 else '-' + str(head)

        rest = numerator % denominator
        res = []
        # 注意到余数只能取0(除尽了),1,2,....denominator-1这么多情况,用字典计算余数出现的最后一次位置，一旦发
        # 生了重复代表从余数上一次在字典中记录的位置开始发生了循环
        rest_dic = {}
        ind = 0
        while rest != 0 and rest not in rest_dic:
            rest_dic[rest] = ind
            rest *= 10
            res.append(str(rest // denominator))
            rest = rest % denominator
            ind += 1

        if not res:
            return head
        if rest == 0:
            return head + '.' + ''.join(res)
        else:
            return head + '.' + ''.join(res[:rest_dic[rest]]) + '(' + ''.join(res[rest_dic[rest]:]) + ')'
