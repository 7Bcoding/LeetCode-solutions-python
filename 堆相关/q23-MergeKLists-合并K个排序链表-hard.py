import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
        [ 1->4->5,
          1->3->4,
          2->6 ]
        """
        if len(lists) == 0 or (lists[0] is None and len(lists) <= 1):
            return None
        n = len(lists)
        dummy = ListNode()
        # 将链表的结点值和结点本身作为元组加入小顶堆中
        tuplelist = [(lists[i].val, lists[i]) for i in range(n) if lists[i]]
        # 构建初始小顶堆
        print(tuplelist)
        if tuplelist:
            heapq.heapify(tuplelist)
            val, heapnode = heapq.heappop(tuplelist)
            node = ListNode(heapnode.val)
        else:
            return None
        # 头节点弹出
        if heapnode.next:
            heapnode = heapnode.next
            heapq.heappush(tuplelist, (heapnode.val, heapnode))
        # 哑结点连接头结点
        dummy.next = node
        while tuplelist:
            # 不断弹出最小值
            val, heapnode = heapq.heappop(tuplelist)
            node.next = ListNode(val)
            node = node.next
            # 继续循环该节点所在链表，取出链表的下一个值，加入小顶堆中，直至链表末尾
            if heapnode.next:
                heapnode = heapnode.next
                heapq.heappush(tuplelist, (heapnode.val, heapnode))
        return dummy.next
