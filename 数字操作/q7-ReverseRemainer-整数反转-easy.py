class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
        reverse_x = 0
        for i in range(100):
            remainder = x % 10
            print(x, remainder)
            reverse_x = reverse_x*10 + remainder
            if x < 10:
                break
            x = x // 10
        print(reverse_x)
        reverse_x = 0 if reverse_x>2**31 else reverse_x
        return reverse_x * flag
