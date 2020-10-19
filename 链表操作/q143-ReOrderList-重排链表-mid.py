class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 解法：线性表
        # 因为链表不支持下标访问，所以我们无法随机访问链表中任意位置的元素。
        # 因此比较容易想到的一个方法是，我们利用线性表存储该链表，然后利用线性
        # 表可以下标访问的特点，直接按顺序访问指定元素，重建该链表即可。
        if not head:
            return

        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None