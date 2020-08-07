class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        # 解法：模拟找规律
        # 连续的0可以视为1个0，连续的1可以视为1个1
        # 比如：001011101
        # 可以视为 010101
        # 因为连续相同的0或1，在反转的时候可以顺便全部反转了。
        # 然后可以从最后一位开始反转，得到：010100
        # 合并最后两个0，变成了：01010
        # 这就又得到下面的规律：
        # 一次反转，可以解决一位。
        # 那么就看合并后的字符串中，第一个'1'后面总共多少位就可以了。若第一位是1，需要额外反转1次，可以直接前面加个'0'统一化处理。
        # 代码实现上，只要统计出从前向后0-1变化次数即可。
        flag = 0
        count = 0
        for i in range(len(target)):
            if target[i] == '0' and flag == 1:
                count += 1
                flag = 0
                continue
            elif target[i] == '1' and flag == 0:
                count += 1
                flag = 1
                continue
        return count
