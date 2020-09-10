class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head, tail):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 解法：模拟
        # 我们需要把链表结点按照 k 个一组分组，所以可以使用一个指针 head 依次指向每组的头结点。
        # 这个指针每次向前移动 k 步，直至链表结尾。对于每个分组，我们先判断它的长度是否大于等于 k。
        # 若是，我们就翻转这部分链表，否则不需要翻转。
        # 接下来的问题就是如何翻转一个分组内的子链表。翻转一个链表并不难，过程可以参考 206. 反转链表。
        # 但是对于一个子链表，除了翻转其本身之外，还需要将子链表的头部与上一个子链表连接，以及子链表的
        # 尾部与下一个子链表连接。
        # 因此，在翻转子链表的时候，我们不仅需要子链表头结点 head，还需要有 head 的上一个结点 pre，以
        # 便翻转完后把子链表再接回 pre。
        # 新建一个结点，把它接到链表的头部，让它作为 pre 的初始值，这样 head 前面就有了一个结点，我们就
        # 可以避开链表头部的边界条件。这么做还有一个好处，下面我们会看到。
        # 反复移动指针 head 与 pre，对 head 所指向的子链表进行翻转，直到结尾。
        # 链表翻转之后，链表的头结点发生了变化，那么应该返回哪个结点呢？
        # 照理来说，前 k 个结点翻转之后，链表的头结点应该是第 k 个结点。那么要在遍历过程中记录第 k 个结点吗？
        # 但是如果链表里面没有 k 个结点，答案又还是原来的头结点。
        # 这个时候就要用到节点 pre了，这个结点一开始被连接到了头结点的前面，而无论之后链表有没有翻转，它的
        # next 指针都会指向正确的头结点。那么我们只要返回它的下一个结点就好了。

        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head, k):
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next

   
