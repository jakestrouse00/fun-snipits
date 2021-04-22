from multiprocessing import Queue, Lock


class CustomQueue:
    def __init__(self, levels: int = 1):
        self._queues = {}
        self._lock = Lock()
        for i in range(levels):
            self._queues[str(i)] = {"queue": Queue(), "size": 0}

    def __repr__(self):
        return f"<Queue: total_levels={len(self._queues.keys())}, level_inputs={','.join(self._queues.keys())}>"

    def put(self, item, level: int):
        """PUT AN ITEM INTO THE QUEUE BASED ON IT'S LEVEL"""
        if 0 <= level <= len(self._queues.keys()):
            with self._lock:
                self._queues[str(level)]["queue"].put(item)
                self._queues[str(level)]["size"] += 1
        else:
            raise Exception("level must be valid")

    def get(self):
        """GET AN ITEM FROM THE FIRST QUEUE"""
        for queue in self._queues.keys():
            if not self._queues[queue]["queue"].empty():
                with self._lock:
                    item = self._queues[queue]["queue"].get()
                    self._queues[queue]["size"] -= 1
                return item
        return None

    def qsize(self) -> object:
        """GET THE SIZE OF THE ENTIRE QUEUE"""
        qsize = 0
        for queue in self._queues.values():
            qsize += queue["size"]
        return qsize


if __name__ == '__main__':
    x = CustomQueue(levels=2)
    print(x)

    x.put("hey", 0)
    x.put("dude", 1)
    print(x.qsize())
    print(x.get())
    print(x.qsize())