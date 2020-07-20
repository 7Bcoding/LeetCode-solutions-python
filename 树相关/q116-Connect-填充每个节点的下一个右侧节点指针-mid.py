
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 解法思路：使用已建立的 next 指针
        # 一棵树中，存在两种类型的 next 指针：
        # 1. 第一种情况是连接同一个父节点的两个子节点。它们可以通过同一个节点直接访问到，因此执行下面操作即可完成连接。
        # 2. 第二种情况在不同父亲的子节点之间建立连接，这种情况不能直接连接。
        # 算法：
        # 1. 从根节点开始，由于第 0 层只有这一个节点，所以不需要连接。直接为第 1 层节点建立 next 指针即可。
        # 该算法中需要注意的一点是，当我们为第 N 层节点建立 next 指针时，处于第 N-1 层。当第 NN 层节
        # 点的 next 指针全部建立完成后，移至第 N 层，建立第 N+1 层节点的 next 指针。
        # 2. 遍历某一层的节点时，这层节点的 next 指针已经建立。因此我们只需要知道这一层的最左节点，就可以按照链表方式遍历，不需要使用队列。

        if not root:
            return root
        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                # CONNECTION 1
                head.left.next = head.right
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                head = head.next

            leftmost = leftmost.left

        return root
