class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# 官方解法：LinkedHashMap原理的实现————哈希表 + 双向链表

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

# 个人解法：哈希表 + 队列
# 1. 达到缓存容量时，最少使用的key从队列中删除
# 2. 每次get/set操作，将操作的key从队列中删除并重新加入到末尾，成为最新使用的key

class LRUCache(object):
    def __init__(self, capacity):

        self.capacity = capacity
        self.queue = []
        self.cache = dict()
        self.res = []

    def get(self, key):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        self.cache[key] = value
        if key not in self.queue:
            self.queue.append(key)
        else:
            self.queue.remove(key)
            self.queue.append(key)
        if self.islimit():
            self.remove()

    def remove(self):
        key = self.queue.pop(0)
        if key in self.cache:
            self.cache.pop(key)

    def islimit(self):
        if len(self.cache) > self.capacity:
            return True
        else:
            return False
