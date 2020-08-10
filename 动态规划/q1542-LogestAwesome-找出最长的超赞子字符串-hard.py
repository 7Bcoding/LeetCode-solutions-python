class Solution:
    def longestAwesome(self, s):

        # 解法：前缀和 + 状态压缩
        # --超赞字符串的条件：一个字符串可以重新排序得到一个回文字符串的充要条件是：对字符计数，出现奇数次的字符个数小于等于1。
        # 1. 状态压缩：因为只关心一个字符出现的次数是奇是偶，因此不需要真正的计数，可用1表示出现奇数次，0表示出现偶数次，更进一
        # 步，数字只有0-9一共10个，可以进行状态压缩。用 status 记录，status & ( 1 << i )表示i出现的奇偶。
        # 那么数字i的数量 +1 即可表示为：
        # status = stauts ^ ( 1 << i ); // 0 ^ 1 = 1 1 ^ 1 = 0
        # 举例：0001 ^ 0001 = 0000，1000 ^ 0001 = 1001，不重复则1补位，重复冲突则为0
        # 2. 前缀和：
        # 使用哈希表 dict{status, index } 记录每个status出现的最左位置index
        # 注意，以0打底作为初始状态为计算的基础，这样才能把端点算进来
        # a. 如果status2和status1相同，那么区间 ( map.get(status1),map.get(status2) ] 中所有数字都出现了偶数次，
        # 满足超赞的条件。
        # b. 如果status2和status1只差一位不同，那么区间 ( map.get(status1),map.get(status2) ] 中有一个数字出现了奇数次，
        # 其余数字都出现了偶数次，满足超赞的条件。

        pre = {0: -1}  # 0打底，记录最初始状态，方便把s[0]统计进来
        status = 0
        re = 0
        for i, v in enumerate(s):
            status = status ^ (1 << int(v))
            # 统计全部为偶数个的情况，在前缀和字典中出现过同样的二进制串
            # 说明除了开区间端点，区间内数字个数都为偶数个
            if status not in pre:
                pre[status] = i
            else:
                re = max(re, i - pre[status])
            # 统计只有一个数字个数为奇数的情况，更新最长超赞子串
            # 方法：每个数字+1 试探，如果得到和之前重复子串，说明这位数字+1后变成了偶数个，
            # 且其他数字都是偶数个，只有这位数字是奇数个，同样满足条件
            for k in range(10):
                new_status = status ^ (1 << k)
                if new_status in pre:
                    re = max(re, i - pre[new_status])
        return re
