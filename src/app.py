import requests
from entropy_pool import EntropyPool

COUNT=50
URL= 'http://www.randomnumberapi.com/api/v1.0/random?count={count}'.format(count=COUNT)

class App():
    def __init__(self):
        self.request_url = URL

        # sets entropy pool upon initialization
        self.setEntropyPool() 

    def __enter__(self):
        return self

    def getData(self):
        # retrieve json response from random number api
        try:
            res = requests.get(self.request_url).json()
            return res
        except Exception as error:
            print(error)
        
        return None

    def setEntropyPool(self):
        # loads data into entropy pool
        data = self.getData()
        self.entropy_pool = EntropyPool(data)

    def getNext(self):
        # gets head value of entropy pool instance
        value = self.entropy_pool.getNext()
        return value

    def randomize(self):
        # prints random data
        next_value = self.getNext()

        if next_value is None:
            # refill entropy pool when it is empty (block)
            self.setEntropyPool()
            self.randomize()
        else:
            # print random value to screen until entropy pool depleted
            print(next_value)
            self.randomize()

    def __exit__(self, type, value, traceback):
        pass