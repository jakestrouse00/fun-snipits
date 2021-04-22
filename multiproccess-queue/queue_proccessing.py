import concurrent.futures
from multiprocessing_priority_queue import CustomQueue


class QueueProcessing:
    def __init__(self, queue, callback_func):
        self._queue = queue
        self._callback = callback_func
        self.processing = False

    def __repr__(self):
        return f"<QueueProcessing: in_use={self.processing}>"

    def process_item(self):
        """GETS THE ITEM FROM THE QUEUE AND SENDS IT TO THE CALLBACK FUNCTION"""
        # print("in")
        item = self._queue.get()
        # print("got")
        self._callback(item)

    def process_queue(self):
        """PROCESSES THE QUEUE. THIS MUST BE REPEATED BY THE MAIN FILE.
        THIS SHOULD ONLY BE CALLED ONCE AT A TIME!"""
        self.processing = True
        qsize = self._queue.qsize()
        # print(qsize)
        with concurrent.futures.ThreadPoolExecutor() as ex:
            for i in range(qsize):
                ex.submit(self.process_item)
        self.processing = False


def test(j):
    print(j)


if __name__ == '__main__':
    x = CustomQueue(levels=2)
    x.put({"1": 2, "3": 4}, 0)
    x.put({"5": 6, "7": 8}, 1)
    p = QueueProcessing(x, test)
    print(p)
    p.process_queue()