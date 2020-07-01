class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
        数字 1-9 在每一行只能出现一次
        数字 1-9 在每一列只能出现一次
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次
        """
        # 解法：一次迭代
        # 如何枚举子数独？——可以使用 box_index = (row / 3) * 3 + columns / 3，获取每个九宫格的子数独，
        # 如何确保行 / 列 / 子数独中没有重复项？
        # 可以利用 value -> count 哈希映射来跟踪所有已经遇到的值。也就是要用到Python的字典
        # 每行有一个字典，每列有一个字典，而每个box字典表示一个九宫格，在各行各列各子数独的9个字典中排除重复项

        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # 查看是否重复出现
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True