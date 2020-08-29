class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 解法1：哈希表
        # 出现过的节点若再次在哈希表出现，则判定为有环
        if head is None or head.next is None:
            return False
        node = head
        nodeset = set()
        while node:
            if node not in nodeset:
                nodeset.add(node)
                node = node.next
            else:
                return True
        return False

    # 解法2: 快慢指针
    # 通过使用具有不同速度的快、慢两个指针遍历链表，空间复杂度可以被降低至O(1)。慢指针每次移动一步，
    # 而快指针每次移动两步。
    # 1. 如果列表中不存在环，最终快指针将会最先到达尾部，此时我们可以返回 false。
    # 现在考虑一个环形链表，把慢指针和快指针想象成两个在环形赛道上跑步的运动员（分别称之为慢跑者与快跑者）。
    # 2. 而快跑者最终一定会追上慢跑者。这是为什么呢？考虑下面这种情况（记作情况 A）-假如快跑者只落后慢跑者一步，
    # 在下一次迭代中，它们就会分别跑了一步或两步并相遇。

    def hasCycle(self, head):
        if not head or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True