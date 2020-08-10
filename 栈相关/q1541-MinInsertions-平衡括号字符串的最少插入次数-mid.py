


class Solution:
    def minInsertions(self, s: str) -> int:

        # 对于括号匹配，第一思路就是栈，遍历字符串，遇到左括号入栈
        # 当遇到右括号时，分两种情况：
        # 1. 有一个连续右括号 ：添加一个右括号
        # 2. 栈空， 添加一个左括号
        # 3. 栈不空，左括号出栈
        # 4. 有两个连续右括号
        # 5. 栈空， 添加一个左括号
        # 6. 栈不空，左括号出栈
        # 最终如果栈为空，那么直接返回所需要添加的个数
        # 如果栈非空，栈长度的2倍加上所需的添加个数即为最终结果
        stack = []
        i = 0
        res = 0
        flag = False
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            # 遇到右括号
            else:
                i += 1
                if i < len(s):
                    if s[i] == ')':
                        if not stack:
                            res += 1
                        else:
                            stack.pop()
                    else:
                        res += 1
                        if not stack:
                            res += 1
                        else:
                            stack.pop()
                        stack.append('(')
                else:
                    flag = True
                    break
            i += 1
        # print(res)
        if not stack:
            if flag:
                return res + 2
            else:
                return res
        else:
            if flag:
                return len(stack) * 2 + res - 1
            else:
                return len(stack) * 2 + res