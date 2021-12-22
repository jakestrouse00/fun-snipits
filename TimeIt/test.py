from libs import TimeIt


def time_consuming_function():
    m = ["1", "2", "3"]

    def haha(k):
        return int(k)

    r = map(haha, m)
    return r


def other_time_consuming_function():
    m = ["1", "2", "3"]

    def haha(k):
        return int(k)

    r = []
    for i in m:
        r.append(haha(i))
    return r


x = TimeIt(time_consuming_function, threaded_operation=True)
time_taken = x.run(cycles=100000)
print(time_taken)

x = TimeIt(other_time_consuming_function, threaded_operation=True)
time_taken = x.run(cycles=100000)
print(time_taken)
