
class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 解法：动态规划
        # 思路：剩下的括号要么在这一组新增的括号内部，要么在这一组新增括号的外部（右侧）。
        # 既然知道了i < n的情况，那我们就可以对所有情况进行遍历：
        # dp[i]表示i对括号的所有排列组合
        # 状态方程：
        # dp[i] = "(" + dp[p]——i=p时所有括号的排列组合 + ")" + dp[q]——i=q时所有括号的排列组合
        # 即 dp[i] = '(' + dp[p] + ')' + dp[i-1-p]
        # 其中 p + q + 1 = n，且 p q 均为非负整数。
        # 事实上，当上述 p 从 0 取到 n-1，q 从 n-1 取到 0 后，所有情况就遍历完了。
        # 注：上述遍历是没有重复情况出现的，即当 (p1,q1)≠(p2,q2) 时，按上述方式取的括号组合一定不同。

        dp = [[] for _ in range(n+1)]         # dp[i]存放i组括号的所有有效组合
        dp[0] = [""]                          # 初始化dp[0]
        for i in range(1, n+1):               # 计算dp[i]
            for p in range(i):                # 遍历p,p从0到i-1
                l1 = dp[p]                    # 得到dp[p]的所有有效组合
                l2 = dp[i-1-p]                # 得到dp[q]的所有有效组合，q从i-1到0
                for k1 in l1:
                    for k2 in l2:
                        dp[i].append("({0}){1}".format(k1, k2))

        return dp[n]