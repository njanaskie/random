import sys
import collections

class EntropyPool():
    def __init__(self, data):
        self.parseData(data)

    def parseData(self, data):
        # parse api response into linked list
        self.pool_list = collections.deque()

        if not data:
            sys.exit()

        for i, value in enumerate(data):
            self.pool_list.append(value)

    def getNext(self):
        # returns head value and removes from linked list instance
        try:
            value = self.pool_list.popleft()
            return value
        except:
            return None
