class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # 解法：动态规划
        # 1. Alice 处在N=k的状态时，他（她）做一步操作，必然使得Bob处于N=m (m < k)的状态。
        # 因此我们只要看是否存在一个 mm 是必败的状态，那么Alice直接执行对应的操作让当前的数字变成 m，
        # Alice 就必胜了，如果没有任何一个是必败的状态的话，说明Alice无论怎么进行操作，最后都会让Bob
        # 处于必胜的状态，此时Alice是必败的。
        #
        # 结合以上我们定义f[i] 表示当前数字 i 的时候先手是处于必胜态还是必败态，true 表示先手必胜，false
        # 表示先手必败，从前往后递推，根据我们上文的分析，枚举i在(0, i)中 i 的因数 j，看是否存在f[i-j]为必败态即可。

        dp = [False] * (N+5)
        dp[1] = False
        dp[2] = True
        for i in range(3, N+1):
            for j in range(1, i):
                if i % j == 0 and dp[i-j] is False:
                    dp[i] = True
                    break

        return dp[N]
