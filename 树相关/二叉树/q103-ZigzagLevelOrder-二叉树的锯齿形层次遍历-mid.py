class TreeNode():
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
                3
              /  \
             9   20
            /     \
           15      7
          返回锯齿形层次遍历如下：
          [[3],[20,9],[15,7]]
        """
        # 解法：
        #    使用两个栈，其中一个栈作为辅助栈
        # 1. A栈弹出节点时，将节点的左子节点先入B栈，右子节点后入B栈
        # 2. 同理，B栈弹出节点时，将节点的左子节点先入A栈，右子节点后入A栈
        # 3. 用'r'换行，每次遇到'r'将'r'插入另一个栈的栈底，并将这一行的
        #    结果lineresult加入result，并清空lineresult
        # 4. 当遇到某个栈只剩下'r'，且另一个栈已为空时，直接退出大循环(否则会无限循环)
        result = []
        if root is None:
            return result
        stack_A = ['r', root]
        stack_B = []

        lineresult = []
        while stack_A or stack_B:
            while stack_A:
                node = stack_A.pop()
                if node:
                    if isinstance(node, TreeNode):
                        lineresult.append(node.val)
                        stack_B.append(node.left)
                        stack_B.append(node.right)
                    else:
                        stack_B.insert(0, 'r')
                        result.append(lineresult)
                        lineresult = []
            if len(stack_B) == 1 and stack_B[0] == 'r':
                break
            while stack_B:
                node = stack_B.pop()
                if node:
                    if isinstance(node, TreeNode):
                        lineresult.append(node.val)
                        stack_A.append(node.right)
                        stack_A.append(node.left)
                    else:
                        stack_A.insert(0, 'r')
                        result.append(lineresult)
                        lineresult = []
            if len(stack_A) == 1 and stack_A[0] == 'r':
                break
        result.pop()
        return result