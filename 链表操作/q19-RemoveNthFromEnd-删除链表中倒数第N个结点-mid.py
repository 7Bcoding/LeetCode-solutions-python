class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 解法：双指针
        #   只使用一次遍历。我们可以使用两个指针而不是一个指针。第一个指针从列表的开头向前移动 n+1步，
        # 而第二个指针将从列表的开头出发。
        #   现在，这两个指针被 n 个结点分开。我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个
        # 指针到达最后一个结点。此时第二个指针将指向从最后一个结点数起的第 n 个结点。我们重新链接第二个
        # 指针所引用的结点的 next 指针指向该结点的下下个结点。
        dummy = ListNode(-1)
        dummy.next = head
        p1, p2 = dummy, dummy

        for i in range(0, n+1):  # 往前移动n+1次
            p2 = p2.next

        while p2:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return dummy.next
