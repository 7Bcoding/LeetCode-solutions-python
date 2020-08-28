class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # 解法：哈希表 + 队列
        # 1. 达到缓存容量时，最少使用的key从队列中删除
        # 2. 每次get/set操作，将操作的key从队列中删除并重新加入到末尾，成为最新使用的key
        self.capacity = capacity
        self.queue = []
        self.lru_cache = dict()
        self.res = []

    def get(self, key):
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
        if key in self.lru_cache:
            return self.lru_cache[key]
        else:
            return -1

    def put(self, key, value):
        self.lru_cache[key] = value
        if key not in self.queue:
            self.queue.append(key)
        else:
            self.queue.remove(key)
            self.queue.append(key)
        if self.islimit():
            self.remove()

    def remove(self):
        key = self.queue.pop(0)
        if key in self.lru_cache:
            self.lru_cache.pop(key)

    def islimit(self):
        if len(self.lru_cache) > self.capacity:
            return True
        else:
            return False

