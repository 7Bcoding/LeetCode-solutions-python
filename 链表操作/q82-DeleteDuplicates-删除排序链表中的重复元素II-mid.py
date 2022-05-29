class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 解法：
        # 由于给定的链表是排好序的，因此重复的元素在链表中出现的位置是连续的，
        # 因此我们只需要对链表进行一次遍历，就可以删除重复的元素。
        # 1. 一次遍历，记录一个dummy哑结点
        # 2. 通过curr.next和curr.next.next的值比较，判断是否删除该重复值
        # 3.
        # 由于链表的头节点可能会被删除，因此我们需要额外使用一个哑节点dummy_node指向链表的头节点。
        # 具体地，我们从指针 cur 指向链表的哑节点，随后开始对链表进行遍历。
        # 如果当前 cur.next 与 cur.next.next 对应的元素相同，
        # 那么我们就需要将 cur.next 以及所有后面拥有相同元素值的链表节点全部删除。我们记下这个元素值 x，
        # 随后不断将 cur.next 从链表中移除，直到 cur.next 为空节点或者其元素值不等于 x 为止。
        # 此时，我们将链表中所有元素值为 xx 的节点全部删除。
        #
        # 如果当前 cur.next 与 cur.next.next 对应的元素不相同，
        # 那么说明链表中只有一个元素值为 cur.next 的节点，那么我们就可以将 cur 指向 cur.next。
        #
        # 当遍历完整个链表之后，我们返回链表的的哑节点的下一个节点 dummy.next 即可。

        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next