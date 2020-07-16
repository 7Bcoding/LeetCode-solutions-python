
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        dummy_odd = ListNode()      # 奇数节点的哑结点
        dummy_even = ListNode()     # 偶数节点的哑结点
        dummy_odd.next = head
        dummy_even.next = head.next

        oddnode = head
        evennode = head.next
        while oddnode and evennode:
            if oddnode.next.next:
                oddnode.next = oddnode.next.next
                oddnode = oddnode.next
            else:
                evennode.next = None
                oddnode.next = dummy_even.next
                break
            if evennode.next.next:
                evennode.next = evennode.next.next
                evennode = evennode.next
            else:
                evennode.next = evennode.next.next
                oddnode.next = dummy_even.next
                break
        return dummy_odd.next