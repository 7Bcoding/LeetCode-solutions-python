class CQueue(object):

    def __init__(self):
        self.stackQueue = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stackQueue.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stackQueue:
            num = self.stackQueue.pop(0)
        else:
            num = -1

        return num
