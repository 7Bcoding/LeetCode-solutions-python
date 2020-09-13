class Solution:
    def breakfastNumber(self, staple, drinks, x):
        staple.sort()
        drinks.sort()
        # 解法：双指针
        j = len(drinks) - 1
        ans = 0
        for i in range(len(staple)):
            while j >= 0 and drinks[j] + staple[i] > x:
                j -= 1
            ans += j + 1

        return ans % 1000000007
