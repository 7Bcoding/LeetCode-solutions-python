class Solution(object):
    def getIntersect(self, head):
        # 解法：Floyd算法
        # 阶段1：相遇
        # 环中的节点从 0 到 C-1 编号，其中 C 是环的长度。非环节点从 -F 到 -1 编号，其中 F 是环以外节点的数目。
        # F 次迭代以后，慢指针指向了 0 且快指针指向某个节点 h ，其中 F = h(modC) 。这是因为快指针在 F 次迭代中
        # 遍历了 2F 个节点，且恰好有 F 个在环中。继续迭代 C-h 次，慢指针显然指向第 C-h 号节点，而快指针也会指向
        # 相同的节点。原因在于，快指针从 h 号节点出发遍历了 2(C-h) 个节点。
        # h + 2(C-h) = 2C - h
        #            = C-h (mod C)
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # 阶段2：找环的入口
        # 给定阶段 1 找到的相遇点，阶段 2 将找到环的入口。首先我们初始化额外的两个指针： ptr1 ，
        # 指向链表的头， ptr2 指向相遇点。然后，我们每次将它们往前移动一步，直到它们相遇，它们相
        # 遇的点就是环的入口，返回这个节点。
        #
        # 我们利用已知的条件：慢指针移动 1 步，快指针移动 2 步，来说明它们相遇在环的入口处。
        # （下面证明中的 slow 表示慢指针，fast 表示快指针）
        # 2 * distance(slow) = distance(fast)
        #             2(F+a) = F+a+b+a
        #              2F+2a = F+2a+b
        #                  F = b
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
