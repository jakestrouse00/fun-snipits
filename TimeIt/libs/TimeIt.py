import time
from concurrent.futures import ThreadPoolExecutor


class TimeIt:
    def __init__(self, callback_func, threaded_operation: bool = True):
        self.threaded_operation = threaded_operation
        self.runs = []
        self.callback_func = callback_func

    def _threaded_operation(self):
        start_time = time.time()
        self.callback_func()
        end_time = time.time()
        run_time = end_time - start_time
        self.runs.append(run_time)

    def run(self, cycles: int):
        if self.threaded_operation:
            with ThreadPoolExecutor() as ex:
                futures = []
                for _ in range(cycles):
                    m = ex.submit(self._threaded_operation)
                    futures.append(m)
        else:
            for cycle in range(cycles):
                start_time = time.time()
                self.callback_func()
                end_time = time.time()
                run_time = end_time - start_time
                self.runs.append(run_time)
        sum_of_runs = sum(self.runs)
        len_of_runs = len(self.runs)
        avg_time = sum_of_runs / len_of_runs
        return avg_time

